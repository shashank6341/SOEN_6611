import unittest
from statistics import Statistics

class TestStatistics(unittest.TestCase):
    """Test suite for the Statistics class."""

    def setUp(self):
        """Setup a fresh instance of Statistics for each test."""
        self.stats = Statistics()
        print("\nSetting up a new instance for testing.")

    def test_read_data_valid(self):
        """Test read_data with valid input."""
        data = [5, 3, 2, 8]
        self.stats.read_data(data)
        self.assertEqual(self.stats.data, [2, 3, 5, 8])  # Assuming data is sorted
        print("Valid data reading test ✅.")

    def test_read_data_invalid(self):
        """Test read_data with invalid input (not a list)."""
        with self.assertRaises(ValueError):
            self.stats.read_data("not a list")
        print("Test Invalid Dataset ✅.")

    def test_read_data_non_numeric(self):
        """Test read_data with a list containing non-numeric values."""
        with self.assertRaises(ValueError):
            self.stats.read_data([1, 'two', 3])
        print("Test data read with non-numeric values ✅.")


    def test_min(self):
        """Test min method on a non-empty dataset."""
        self.stats.read_data([4, 1, 5])
        self.assertEqual(self.stats.min(), 1)
        print("Test Minimum on an non-empty data set ✅.")

    def test_min_empty(self):
        """Test min method on an empty dataset."""
        with self.assertRaises(ValueError):
            self.stats.min()
        print("Test Minimum on empty data set ✅.")

    def test_max(self):
        """Test max method on a non-empty dataset."""
        self.stats.read_data([3, 6, 2])
        self.assertEqual(self.stats.max(), 6)
        print("Test Maximum on actual data set ✅.")

    def test_max_empty(self):
        """Test max method on an empty dataset."""
        with self.assertRaises(ValueError):
            self.stats.max()
        print("Test Maximum on empty data set ✅.")

    def test_mode(self):
        """Test mode method on a dataset with a clear mode."""
        self.stats.read_data([1, 2, 2, 3])
        self.assertEqual(self.stats.mode(), [2])
        print("Test Mode on dataset ✅.")

    def test_mode_empty(self):
        """Test mode method on an empty dataset."""
        self.stats.read_data([])
        self.assertEqual(self.stats.mode(), [])
        print("Test Mode on empty data set ✅.")

    def test_mode_multiple_modes(self):
        """Test mode method on a dataset with multiple modes."""
        self.stats.read_data([1, 1, 2, 2, 3])
        self.assertEqual(sorted(self.stats.mode()), [1, 2])
        print("Test Mode on dataset with multiple modes ✅.")


    def test_median(self):
        """Test median method on an odd-length dataset."""
        self.stats.read_data([3, 1, 4])
        self.assertEqual(self.stats.median(), 3)
        print("Test Median on odd-length data set ✅.")

    def test_median_even(self):
        """Test median method on an even-length dataset."""
        self.stats.read_data([1, 2, 3, 4])
        self.assertEqual(self.stats.median(), 2.5)
        print("Test Median on even-length data set ✅.")

    def test_median_empty(self):
        """Test median method on an empty dataset."""
        with self.assertRaises(ValueError):
            self.stats.median()
        print("Test Median on empty data set ✅.")

    def test_mean(self):
        """Test mean method on a non-empty dataset."""
        self.stats.read_data([1, 2, 3, 4])
        self.assertAlmostEqual(self.stats.mean(), 2.5)
        print("Test Mean on a non empty data set ✅.")

    def test_mean_empty(self):
        """Test mean method on an empty dataset."""
        with self.assertRaises(ValueError):
            self.stats.mean()
        print("Test Mean on an empty data set ✅.")

    def test_mad(self):
        """Test mad (Mean Absolute Deviation) method on a non-empty dataset."""
        self.stats.read_data([1, 2, 3])
        self.assertAlmostEqual(self.stats.mad(), 0.6667, places=4)
        print("Test mad (Mean Absolute Deviation) method on a non-empty dataset ✅")

    def test_mad_empty(self):
        """Test mad method on an empty dataset."""
        with self.assertRaises(ValueError):
            self.stats.mad()
        print("Test Mean Absolute Deviation method on an empty dataset ✅")

    def test_stdev(self):
        """Test standard deviation method on a non-empty dataset."""
        self.stats.read_data([10, 12, 23, 23, 16, 23, 21, 16])
        self.assertAlmostEqual(self.stats.stdev(), 5.2372, places=4)
        print("Test standard deviation method on an non-empty dataset ✅")

    def test_stdev_single_data_point(self):
        """Test standard deviation method on a dataset with a single data point."""
        self.stats.read_data([4])
        with self.assertRaises(ValueError):
            self.stats.stdev()
        print("Test standard deviation on a dataset with a single data point ✅.")

    def test_stdev_empty(self):
        """Test standard deviation method on an empty dataset."""
        with self.assertRaises(ValueError):
            self.stats.stdev()
        print("Test standard deviation method on an empty dataset ✅")

    def test_sqrt(self):
        """Test sqrt method with a positive number."""
        self.assertAlmostEqual(self.stats.sqrt(16), 4)
        print("Test Square root method with positive number ✅")

    def test_sqrt_zero(self):
        """Test sqrt method with zero."""
        self.assertAlmostEqual(self.stats.sqrt(0), 0)
        print("Test Square root method with zero ✅.")


    def test_sqrt_negative(self):
        """Test sqrt method with a negative number."""
        with self.assertRaises(ValueError):
            self.stats.sqrt(-1)
        print("Test Square Root method with a negavtive number ✅")

    def test_variance(self):
        """Test variance method on a dataset with sufficient data points."""
        self.stats.read_data([1, 2, 3, 4, 5])
        self.assertAlmostEqual(self.stats.variance(), 2.5)
        print("Test variance method on a dataset with sufficient data points ✅")

    def test_variance_insufficient_data(self):
        """Test variance method on a dataset with insufficient data points."""
        self.stats.read_data([1])
        with self.assertRaises(ValueError):
            self.stats.variance()
        print("Test variance method on a dataset with in-sufficient data points ✅")

if __name__ == '__main__':
    unittest.main()
