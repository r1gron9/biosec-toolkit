"""
Tests for compare_sequences module
"""
import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import compare_sequences


class TestCompareSequences(unittest.TestCase):
    """Test cases for sequence comparison functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.seq1 = "ATGCTAGCTAGC"
        self.seq2 = "ATGCAAGCTAGC"

    def test_display_results_returns_string(self):
        """Test that display_results returns HTML string"""
        result = compare_sequences.display_results(
            self.seq1, self.seq2,
            optimizer1="Test1",
            optimizer2="Test2"
        )
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_display_results_contains_html_tags(self):
        """Test that result contains HTML formatting"""
        result = compare_sequences.display_results(
            self.seq1, self.seq2,
            optimizer1="Test1",
            optimizer2="Test2"
        )
        self.assertIn("<", result)
        self.assertIn(">", result)

    def test_color_triplet_comparison_output(self):
        """Test color_triplet_comparison functionality"""
        from Bio.Seq import Seq
        seq1 = Seq(self.seq1)
        seq2 = Seq(self.seq2)
        
        colored1, colored2 = compare_sequences.color_triplet_comparison(seq1, seq2)
        
        self.assertIsInstance(colored1, str)
        self.assertIsInstance(colored2, str)
        self.assertTrue(len(colored1) > 0)
        self.assertTrue(len(colored2) > 0)

    def test_count_triplet_differences(self):
        """Test counting of triplet differences"""
        from Bio.Seq import Seq
        seq1 = Seq(self.seq1)
        seq2 = Seq(self.seq2)
        
        counts = compare_sequences.count_triplet_differences(seq1, seq2)
        
        self.assertIsInstance(counts, list)
        self.assertEqual(len(counts), 3)
        self.assertTrue(all(isinstance(c, int) for c in counts))

    def test_find_motifs(self):
        """Test motif finding in sequences"""
        sequence = "ATGCTATAATAGC"
        motifs = ["TATAAT"]
        
        highlighted, found = compare_sequences.find_motifs(sequence, motifs)
        
        self.assertIsInstance(highlighted, str)
        self.assertIsInstance(found, list)


if __name__ == '__main__':
    unittest.main()
