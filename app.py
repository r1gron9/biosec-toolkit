from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import sys
from werkzeug.utils import secure_filename
from modules import compare_sequences, search_promoter_motif, search_motifs_quantity, generate_test_file, inject_motif

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # When running from .exe
    except Exception:
        base_path = os.path.abspath(".")  # When running from script
    return os.path.join(base_path, relative_path)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, template_folder=resource_path('templates'), static_folder=resource_path('static'))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/compare-sequences', methods=['GET', 'POST'])
def compare_sequences_route():
    result = None
    if request.method == 'POST':
        optimizer1 = request.form['optimizer1']
        optimizer2 = request.form['optimizer2']
        sequence1 = request.form['sequence1']
        sequence2 = request.form['sequence2']
        result = compare_sequences.display_results(sequence1, sequence2, optimizer1, optimizer2)
    return render_template('compare_sequences.html', result=result)

@app.route('/search-promoter-motif', methods=['GET', 'POST'])
def search_promoter_motif_route():
    result = None
    if request.method == 'POST':
        csv_file = request.files['csv_file']
        fasta_file = request.files['fasta_file']
        if csv_file and fasta_file:
            csv_filename = secure_filename(csv_file.filename)
            fasta_filename = secure_filename(fasta_file.filename)
            csv_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_filename)
            fasta_path = os.path.join(app.config['UPLOAD_FOLDER'], fasta_filename)
            csv_file.save(csv_path)
            fasta_file.save(fasta_path)
            result = search_promoter_motif.process_files(csv_path, fasta_path)
    return render_template('search_promoter_motif.html', result=result)

@app.route("/search-motif-quantity", methods=["GET", "POST"])
def search_motifs_quantity_route():
    results = None
    if request.method == "POST":
        csv_file = request.files.get("csv_file")
        if csv_file:
            filename = secure_filename(csv_file.filename)
            csv_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            csv_file.save(csv_path)
            results = search_motifs_quantity.search_motif(csv_path)
    return render_template("search_motifs_quantity.html", results=results)

@app.route('/generate_test_file', methods=['GET', 'POST'])
def generate_test_file_route():
    if request.method == 'POST':
        num_sequences = int(request.form['num_sequences'])
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'generated_test_motif_inject.csv')
        generate_test_file.generate_test_file(total_sequences=num_sequences, output_path=output_path)
        return send_file(output_path, as_attachment=True)
    return render_template('generate_test_file.html')


@app.route('/inject-motif', methods=['GET', 'POST'])
def inject_motif_route():
    results = None
    output_filename = None
    if request.method == 'POST':
        csv_file = request.files['csv_file']
        if csv_file:
            output_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'inject_motif_output.csv')
            csv_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(csv_file.filename))
            csv_file.save(csv_path)
            results = inject_motif.process_csv(csv_path, output_filename)
    return render_template('inject_motif.html', results=results, output_filename=output_filename)

@app.route('/download-inject-motif-output')
def download_inject_output_route():
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'inject_motif_output.csv')
    return send_file(output_path, as_attachment=True)

@app.route('/download-example-full-genome-fasta')
def download_example_full_genome_fasta_route():
    example_path = resource_path('examples/example_E-coli.fasta')
    return send_file(example_path, as_attachment=True)

@app.route('/download-example-full-genome-csv')
def download_example_full_genome_csv_route():
    example_path = resource_path('examples/example_genes_full_genome.csv')
    return send_file(example_path, as_attachment=True)

@app.route('/download-example-multiple-sequences')
def download_example_multiple_sequences_route():
    example_path = resource_path('examples/example_multiple_sequences.csv')
    return send_file(example_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)