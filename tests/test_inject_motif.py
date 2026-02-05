"""
Tests for inject_motif module
"""
import unittest
import sys
import os
import tempfile
import pandas as pd

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import inject_motif


class TestInjectMotif(unittest.TestCase):
    """Test cases for motif injection functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.dna_seq = "ATGAAACGATAA"
        self.protein_seq = "MKR*"

    def test_insert_attata_motif_returns_tuple(self):
        """Test that insert_attata_motif returns correct structure"""
        result = inject_motif.insert_attata_motif(self.dna_seq, self.protein_seq)
        
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 4)

    def test_insert_attata_motif_returns_string_sequence(self):
        """Test that modified sequence is a string"""
        modified_seq, num_ins, changes, cases = inject_motif.insert_attata_motif(
            self.dna_seq, self.protein_seq
        )
        
        self.assertIsInstance(modified_seq, str)
        self.assertIsInstance(num_ins, int)

    def test_insert_attata_motif_preserves_length(self):
        """Test that sequence length is preserved or handled correctly"""
        modified_seq, num_ins, changes, cases = inject_motif.insert_attata_motif(
            self.dna_seq, self.protein_seq
        )
        
        # Modified sequence should be same length or modified appropriately
        self.assertIsInstance(modified_seq, str)
        self.assertTrue(len(modified_seq) > 0)

    def test_process_csv_creates_output(self):
        """Test that process_csv creates output CSV"""
        # Create temporary test CSV
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            test_csv = f.name
            # Write test data
            df = pd.DataFrame({
                'predicted_dna': ['ATGAAACGATAA', 'ATGATACGATAA'],
                'protein_sequence': ['MKR*', 'MIR*']
            })
            df.to_csv(test_csv, index=False)

        try:
            # Create output path
            with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
                output_csv = f.name

            # Process CSV
            results = inject_motif.process_csv(test_csv, output_csv)

            # Check output
            self.assertIsInstance(results, dict)
            self.assertIn('total_sequences', results)
            self.assertTrue(os.path.exists(output_csv))

            # Clean up output
            if os.path.exists(output_csv):
                os.remove(output_csv)
        finally:
            # Clean up input
            if os.path.exists(test_csv):
                os.remove(test_csv)

    def test_process_csv_returns_dict(self):
        """Test that process_csv returns dictionary with expected keys"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            test_csv = f.name
            df = pd.DataFrame({
                'predicted_dna': ['ATGAAACGATAA'],
                'protein_sequence': ['MKR*']
            })
            df.to_csv(test_csv, index=False)

        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
                output_csv = f.name

            results = inject_motif.process_csv(test_csv, output_csv)

            expected_keys = [
                'total_sequences',
                'sequences_with_existing_motif',
                'sequences_without_motif'
            ]
            
            for key in expected_keys:
                self.assertIn(key, results)

            if os.path.exists(output_csv):
                os.remove(output_csv)
        finally:
            if os.path.exists(test_csv):
                os.remove(test_csv)


if __name__ == '__main__':
    unittest.main()
