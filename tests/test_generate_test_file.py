"""
Tests for generate_test_file module
"""
import unittest
import sys
import os
import tempfile
import pandas as pd

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import generate_test_file


class TestGenerateTestFile(unittest.TestCase):
    """Test cases for synthetic sequence generation"""

    def test_generate_test_file_creates_file(self):
        """Test that generate_test_file creates output CSV"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            output_path = f.name

        try:
            # Generate test file
            result = generate_test_file.generate_test_file(
                total_sequences=10,
                output_path=output_path
            )

            # Check file was created
            self.assertTrue(os.path.exists(output_path))
            
            # Check file has content
            df = pd.read_csv(output_path)
            self.assertEqual(len(df), 10)
        finally:
            if os.path.exists(output_path):
                os.remove(output_path)

    def test_generate_test_file_has_required_columns(self):
        """Test that generated file has required columns"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            output_path = f.name

        try:
            generate_test_file.generate_test_file(
                total_sequences=5,
                output_path=output_path
            )

            df = pd.read_csv(output_path)
            
            required_columns = ['predicted_dna', 'protein_sequence', 'expected_case']
            for col in required_columns:
                self.assertIn(col, df.columns)
        finally:
            if os.path.exists(output_path):
                os.remove(output_path)

    def test_generate_test_file_dna_not_empty(self):
        """Test that generated DNA sequences are not empty"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            output_path = f.name

        try:
            generate_test_file.generate_test_file(
                total_sequences=5,
                output_path=output_path
            )

            df = pd.read_csv(output_path)
            
            for dna in df['predicted_dna']:
                self.assertTrue(len(dna) > 0)
                self.assertTrue(all(c in 'ATGC' for c in dna.upper()))
        finally:
            if os.path.exists(output_path):
                os.remove(output_path)

    def test_generate_test_file_protein_not_empty(self):
        """Test that generated protein sequences are not empty"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            output_path = f.name

        try:
            generate_test_file.generate_test_file(
                total_sequences=5,
                output_path=output_path
            )

            df = pd.read_csv(output_path)
            
            for protein in df['protein_sequence']:
                self.assertTrue(len(protein) > 0)
        finally:
            if os.path.exists(output_path):
                os.remove(output_path)

    def test_generate_case_sequence(self):
        """Test case sequence generation"""
        for case_num in [1, 2, 3]:
            seq, offset = generate_test_file.generate_case_sequence(case_num)
            
            self.assertIsInstance(seq, str)
            self.assertIsInstance(offset, int)
            self.assertTrue(len(seq) > 0)
            self.assertTrue(offset > 0)
            # Sequence should be divisible by 3 (codon)
            self.assertEqual(len(seq) % 3, 0)


if __name__ == '__main__':
    unittest.main()
