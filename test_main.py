#!/usr/bin/env python3
"""
Test suite for the Snack Machine program.
These tests verify that the program runs correctly.
"""

import pytest
from unittest.mock import patch
from io import StringIO
import main


class TestSnackMachine:
    """Basic tests to verify the snack machine works correctly."""
    
    def test_valid_choice_1(self, capsys):
        """Test that choice 1 (Chips) works correctly."""
        with patch('builtins.input', return_value='1'):
            main.main()
            captured = capsys.readouterr()
            assert "Chips" in captured.out
            assert "$1.50" in captured.out
            assert "Great choice!" in captured.out
    
    def test_valid_choice_2(self, capsys):
        """Test that choice 2 (Chocolate Bar) works correctly."""
        with patch('builtins.input', return_value='2'):
            main.main()
            captured = capsys.readouterr()
            assert "Chocolate Bar" in captured.out
            assert "$2.00" in captured.out
            assert "Great choice!" in captured.out
    
    def test_valid_choice_3(self, capsys):
        """Test that choice 3 (Granola Bar) works correctly."""
        with patch('builtins.input', return_value='3'):
            main.main()
            captured = capsys.readouterr()
            assert "Granola Bar" in captured.out
            assert "$1.25" in captured.out
            assert "Great choice!" in captured.out
    
    def test_valid_choice_4(self, capsys):
        """Test that choice 4 (Soda) works correctly."""
        with patch('builtins.input', return_value='4'):
            main.main()
            captured = capsys.readouterr()
            assert "Soda" in captured.out
            assert "$1.75" in captured.out
            assert "Great choice!" in captured.out
    
    def test_invalid_choice_5(self, capsys):
        """Test that an invalid choice (5) is handled correctly."""
        with patch('builtins.input', return_value='5'):
            main.main()
            captured = capsys.readouterr()
            assert "Invalid selection" in captured.out
    
    def test_invalid_choice_letter(self, capsys):
        """Test that an invalid choice (letter) is handled correctly."""
        with patch('builtins.input', return_value='a'):
            main.main()
            captured = capsys.readouterr()
            assert "Invalid selection" in captured.out
    
    def test_welcome_message_displayed(self, capsys):
        """Test that the welcome message is displayed."""
        with patch('builtins.input', return_value='1'):
            main.main()
            captured = capsys.readouterr()
            assert "Welcome to the Python Snack Machine!" in captured.out
    
    def test_menu_displayed(self, capsys):
        """Test that the menu is displayed to users."""
        with patch('builtins.input', return_value='1'):
            main.main()
            captured = capsys.readouterr()
            assert "Available snacks:" in captured.out
            assert "Chips" in captured.out
            assert "Chocolate Bar" in captured.out
            assert "Granola Bar" in captured.out
            assert "Soda" in captured.out
