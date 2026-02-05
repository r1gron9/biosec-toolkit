"""
Tests for search_promoter_motif module
"""
import unittest
import sys
import os
import tempfile
import csv

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import search_promoter_motif


class TestSearchPromoterMotif(unittest.TestCase):
    """Test cases for promoter motif searching"""

    def setUp(self):
        """Create temporary test data files"""
        # Create temporary FASTA file
        self.fasta_file = tempfile.NamedTemporaryFile(
            mode='w', 
            suffix='.fasta', 
            delete=False
        )
        self.fasta_file.write(">sequence1\n")
        self.fasta_file.write("ATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATG\n")
        self.fasta_file.close()

        # Create temporary genes CSV file with correct format
        self.genes_file = tempfile.NamedTemporaryFile(
            mode='w', 
            suffix='.csv', 
            delete=False
        )
        writer = csv.writer(self.genes_file)
        # Header row (required)
        writer.writerow(['Accession', 'Start', 'Stop', 'Gene_symbol', 'Strand', 'NCBI_Gene_ID', 'Name'])
        # Data row (starts at position 1 in the file)
        writer.writerow(['NC_000001.11', '1', '50', 'GENE1', '+', '12345', 'test_gene_1'])
        writer.writerow(['NC_000001.11', '60', '100', 'GENE2', '+', '12346', 'test_gene_2'])
        self.genes_file.close()

    def tearDown(self):
        """Clean up temporary files"""
        if os.path.exists(self.fasta_file.name):
            os.remove(self.fasta_file.name)
        if os.path.exists(self.genes_file.name):
            os.remove(self.genes_file.name)

    def test_load_genes(self):
        """Test loading gene information from CSV"""
        genes = search_promoter_motif.load_genes(self.genes_file.name)
        
        # Returns a DataFrame, not a list
        import pandas as pd
        self.assertIsInstance(genes, pd.DataFrame)
        # The function removes the header row (iloc[1:])
        # so we should have 1 row (the second row from CSV)
        self.assertGreater(len(genes), 0)
        # Check that the basic columns exist
        self.assertIn('Start', genes.columns)
        self.assertIn('Stop', genes.columns)

    def test_load_fasta_sequence(self):
        """Test loading FASTA sequences"""
        sequence = search_promoter_motif.load_fasta_sequence(self.fasta_file.name)
        
        self.assertIsInstance(sequence, str)
        self.assertTrue(len(sequence) > 0)
        # Should contain expected nucleotides
        self.assertTrue(all(c in 'ATGC' for c in sequence))

    def test_search_attata_in_sequence(self):
        """Test ATTATA searching"""
        genes = search_promoter_motif.load_genes(self.genes_file.name)
        test_dna = "ATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATGATG"
        
        # search_attata requires both sequence and genes
        result = search_promoter_motif.search_attata(test_dna, genes)
        
        self.assertIsNotNone(result)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)  # Should return (indices, count, total_searches)

    def test_search_attata_not_found(self):
        """Test ATTATA search when motif not present"""
        genes = search_promoter_motif.load_genes(self.genes_file.name)
        test_dna = "AAAAAAGGGGGGTTTTTGGGGGGTTTTTCCCCCC"
        
        result = search_promoter_motif.search_attata(test_dna, genes)
        
        # Result should be a tuple (indices, count, total_searches)
        self.assertIsInstance(result, tuple)
        # Count should be 0 (no ATTATA found)
        self.assertEqual(result[1], 0)

    def test_process_files(self):
        """Test processing of genes and FASTA files"""
        # This is an integration test
        result = search_promoter_motif.process_files(
            self.genes_file.name,
            self.fasta_file.name
        )
        
        # Result should be a list or dict
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
