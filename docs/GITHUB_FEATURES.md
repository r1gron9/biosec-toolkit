# GitHub Pages for biosec-toolkit

This directory contains the GitHub Pages configuration for the biosec-toolkit documentation.

## Features

- **Search functionality** - Integrated with GitHub's built-in search
- **Jupyter Notebook rendering** - GitHub automatically renders `.ipynb` files
- **Quick navigation** - Easy links to all resources
- **Interactive examples** - Notebook can be run in-browser via Binder

## Accessing the Notebook

The interactive Jupyter notebook is available at:
https://github.com/r1gron9/biosec-toolkit/blob/main/queries/queries_examples.ipynb

Click the notebook file to view it rendered by GitHub with full syntax highlighting.

## Running Notebooks Online (via Binder)

To run the notebook interactively in your browser (no installation needed):

1. Go to: https://github.com/r1gron9/biosec-toolkit
2. Copy the repository URL
3. Visit: https://mybinder.org/
4. Paste the URL and launch

Or use this direct link (once set up):
https://mybinder.org/v2/gh/r1gron9/biosec-toolkit/main?filepath=queries/queries_examples.ipynb

## GitHub Search Features

### Full-text search
- Use GitHub's search bar at the top of the repository
- Search for specific functions, motifs, or concepts
- Results include code and documentation

### Advanced search
- Search in specific files: `in:file:queries/run_queries.py`
- Search in README: `in:file:README.md`
- Search tests: `in:file:tests/`

Example searches:
- `ATTATA in:code` - Find ATTATA references
- `search_motif in:code` - Find function definitions
- `codon in:path:modules` - Find in specific path

## Notebook Features

The `queries_examples.ipynb` includes:

1. **Environment Setup** - Import all necessary libraries
2. **Example 1**: Sequence comparison with HTML output
3. **Example 2**: Promoter motif searching
4. **Example 3**: Motif quantity analysis
5. **Example 4**: Test file generation
6. **Example 5**: ATTATA injection
7. **Complete Workflow**: Full pipeline demonstration

Each example includes:
- Code cells (executable)
- Markdown documentation
- Expected outputs
- Usage instructions

## Setting Up Binder Badge (Optional)

To make it easy for users, add this badge to README.md:

```markdown
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/r1gron9/biosec-toolkit/main?filepath=queries/queries_examples.ipynb)
```

This creates a clickable badge that launches the notebook in Binder.

## Requirements for Binder

Create `requirements.txt` in project root (already exists):
- pandas
- numpy
- biopython
- flask
- tqdm

Binder will install these automatically.

## Features When Viewing Notebook on GitHub

1. **View rendered output** - See plots and tables
2. **Syntax highlighting** - Code is color-coded
3. **Cell-by-cell structure** - Easy navigation
4. **Markdown cells** - Documentation renders nicely
5. **Raw view** - Switch to raw JSON if needed

## Tips for Users

1. **To view the notebook on GitHub**: Click the `.ipynb` file in the `queries/` folder
2. **To edit and run locally**: Clone and use Jupyter locally
3. **To run online without installing**: Use Binder (one-click launch)
4. **To search code**: Use GitHub's search bar

## Files Included

- `queries/queries_examples.ipynb` - Main interactive notebook
- `queries/run_queries.py` - CLI version of all examples
- `queries/README.md` - Module documentation

## Future Enhancements

- [ ] Add GitHub Actions workflow to validate notebooks
- [ ] Create additional notebooks for specific workflows
- [ ] Set up GitHub Pages Jekyll site for custom documentation
- [ ] Add YouTube tutorial links
- [ ] Create video walkthroughs

---

**Start exploring**: Go to the [queries folder](https://github.com/r1gron9/biosec-toolkit/tree/main/queries) to find the notebook!
