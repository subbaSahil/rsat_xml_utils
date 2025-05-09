from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import xmlConverter
import scriptGenerator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded XML file
        xml_file = request.files['xml_file']
        xml_file.save(secure_filename(xml_file.filename))

        # Convert the XML file using xmlConverter
        converted_data = xmlConverter.extract_user_actions(xml_file.filename)

        # Generate a script using scriptGenerator
        script = scriptGenerator.generate_selenium_script(converted_data)

        # Save the output to a new file
        output_file = 'output.py'
        with open(output_file, 'w') as f:
            f.write(script)

        # Return the output file as a download
        return send_file(output_file, as_attachment=True)

    return '''
        <form action="" method="post" enctype="multipart/form-data">
            <input type="file" name="xml_file" accept=".xml">
            <input type="submit" value="Upload and Convert">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)