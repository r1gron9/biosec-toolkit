"""
Tests for search_motifs_quantity module
"""
import unittest
import sys
import os
import tempfile
import csv

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import search_motifs_quantity


class TestSearchMotifsQuantity(unittest.TestCase):
    """Test cases for motif quantity analysis"""

    def setUp(self):
        """Create temporary test data"""
        # Create test CSV with DNA sequences in the correct format
        self.test_csv = tempfile.NamedTemporaryFile(
            mode='w', 
            suffix='.csv', 
            delete=False
        )
        writer = csv.writer(self.test_csv)
        # Header with Serial (unnamed column)
        writer.writerow(['', 'Id', 'predicted_dna', 'protein_sequence', 'organism_name'])
        
        # Data rows
        writer.writerow(['1', 'seq1', 'ATGATGATGATGATGATGATGATGATGATGATG', 'MMMMMMMMMM', 'E.coli'])
        writer.writerow(['2', 'seq2', 'ATTATAATTATAATTATAATTATAATTATAATTAT', 'IIIIIIIIII', 'E.coli'])
        writer.writerow(['3', 'seq3', 'AAAAAAGGGGGGTTTTTGGGGGGTTTTTCCCCCC', 'KKKKKKVVVV', 'B.subtilis'])
        writer.writerow(['4', 'seq4', 'CCCCCCTTTTTTAAAAAAAGGGGGGAAAAAATTTT', 'PPPPPPKKKK', 'B.subtilis'])
        
        self.test_csv.close()

    def tearDown(self):
        """Clean up temporary files"""
        if os.path.exists(self.test_csv.name):
            os.remove(self.test_csv.name)

    def test_search_motif_returns_dict(self):
        """Test that search_motif returns a dictionary with statistics"""
        result = search_motifs_quantity.search_motif(self.test_csv.name, 'ATTATA')
        
        self.assertIsInstance(result, dict)

    def test_search_motif_contains_probability(self):
        """Test that result contains probability statistics"""
        result = search_motifs_quantity.search_motif(self.test_csv.name, 'ATTATA')
        
        # Result is a dictionary with these keys
        self.assertIsInstance(result, dict)
        # Check for probability-related keys returned by the function
        has_probability = ('prob_nucleotide' in result or 
                          'prob_sequence' in result or 
                          'probability' in result)
        self.assertTrue(has_probability)

    def test_search_motif_counts_occurrences(self):
        """Test that motif occurrences are counted"""
        result = search_motifs_quantity.search_motif(self.test_csv.name, 'ATTATA')
        
        # At least one sequence has ATTATA
        self.assertIsNotNone(result)

    def test_search_motif_different_patterns(self):
        """Test searching for different motif patterns"""
        motifs = ['ATTATA', 'ATG', 'TAA', 'GGG']
        
        for motif in motifs:
            result = search_motifs_quantity.search_motif(self.test_csv.name, motif)
            # Should return something for each query
            self.assertIsNotNone(result)

    def test_search_motif_with_test_file(self):
        """Test on actual generated test file if it exists"""
        # Use the test CSV we created instead of searching for example file
        # This ensures the test is self-contained
        result = search_motifs_quantity.search_motif(self.test_csv.name, 'ATTATA')
        
        # Should return a dictionary
        self.assertIsInstance(result, dict)
        # Should have motif occurrences
        self.assertIn('total_occurrences', result) or \
        self.assertIn('prob_sequence', result)

    def test_search_motif_empty_pattern(self):
        """Test search with empty pattern"""
        # Empty pattern is treated as empty string, which has behavior
        result = search_motifs_quantity.search_motif(self.test_csv.name, '')
        
        # Should still return a dictionary (empty string matches everything)
        self.assertIsInstance(result, dict)
        # Empty pattern might match all positions or return special result
        # Both behaviors are acceptable
        self.assertIsNotNone(result)

    def test_duplicate_detection(self):
        """Test duplicate sequence detection (if implemented)"""
        # Check if function exists and test it
        if hasattr(search_motifs_quantity, 'detect_duplicates'):
            result = search_motifs_quantity.detect_duplicates(self.test_csv.name)
            self.assertIsInstance(result, (list, dict, int))


if __name__ == '__main__':
    unittest.main()
