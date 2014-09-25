from io       import StringIO
from unittest import main, TestCase

from Netflix import rmse, netflix_read, netflix_moviecache, netflix_usercache, netflix_panswers, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    # ----
    # rmse
    # ----

    def test_rmse1 (self) :
        a = [1, 2, 3]
        p = [2, 3, 4]
        rmse1 = rmse (a, p)
        self.assertEqual (rmse1, 1)

    def test_rmse2 (self) :
        a = [10, 15, 20]
        p = [15, 20, 25]
        rmse2 = rmse (a, p)
        self.assertEqual (rmse2, 5)

    def test_rmse3 (self) :
        a = [10, 10, 10]
        p = [10, 10, 10]
        rmse3 = rmse (a, p)
        self.assertEqual (rmse3, 0)
    
    def test_rmse4 (self) :
        a = [11, 11, 11]
        p = [10, 10, 10]
        rmse4 = rmse (a, p)
        self.assertEqual (rmse4, 1)

    # ----
    # netflix_read
    # ----

    def test_read1 (self) :
        r = StringIO ("10:\n1\n2\n3\n4")
        read1 = netflix_read (r)
        self.assertEqual (read1, {10: [1, 2, 3, 4]})

    def test_read2 (self) :
        r = StringIO ("70:\n9999\n999999\n9999999999")
        read2 = netflix_read (r)
        self.assertEqual (read2, {70: [9999, 999999, 9999999999]})

    def test_read3 (self) :
        r = StringIO ("1:\n2\n3:\n4\n5:\n6")
        read3 = netflix_read (r)
        self.assertEqual (read3, {1: [2], 3: [4], 5: [6]})

    # ----
    # netflix_moviecache
    # ----

    def test_movie1 (self) :
        r = StringIO ("1": "2")
        movie1 = netflix_moviecache (r)
        self.assertEqual (movie1, {1: 2})

    def test_movie2 (self) :
        r = StringIO ("10": "20", "40": "80")
        movie2 = netflix_moviecache (r)
        self.assertEqual (movie2, {10: 20, 40: 80})

    def test_movie3 (self) :
        r = StringIO ("1": "3.5", "2" : "4.5")
        movie3 = netflix_moviecache (r)
        self.assertEqual (movie3, {1: 3.5, 2: 4.5})

    def test_movie4 (self) :
        r = StringIO ("3": "4", "6" : "8")
        movie4 = netflix_moviecache (r)
        self.assertEqual (movie4, {3: 4, 6: 8})

    # ----
    # netflix_usercache
    # ----

    def test_user1 (self) :
        r = StringIO ("100": "200")
        user1 = netflix_usercache (r)
        self.assertEqual (user1, {100: 200})

    def test_user2 (self) :
        r = StringIO ("2.3": "2.33", "3.4": "3.44")
        user2 = netflix_usercache (r)
        self.assertEqual (user2, {2.3: 2.33, 3.4: 3.44})

    def test_user3 (self) :
        r = StringIO ("1": "2", "3": "4", "5": "6")
        user3 = netflix_usercache (r)
        self.assertEqual (user3, {1: 2, 3: 4, 5: 6})

    def test_user4 (self) :
        r = StringIO ("13": "13")
        user4 = netflix_usercache (r)
        self.assertEqual (user4, {13: 13})

    # ----
    # netflix_panswers
    # ----

    def test_panswers1 (self) :
        r = StringIO ({"1798 1663145": 4})
        panswers1 = netflix_panswers (r)
        self.assertEqual (panswers1, {"1798 1663145": 4})

    def test_panswers2 (self) :
        r = StringIO ({"13439 2072670": 3, "3864 2299969": 3})
        panswers2 = netflix_panswers (r)
        self.assertEqual (panswers2, {"13439 2072670": 3, "3864 2299969": 3})

    def test_panswers3 (self) :
        r = StringIO ({"4932 1735937": 5, "11607 1906698": 5, "483 1939265": 1})
        panswers3 = netflix_panswers (r)
        self.assertEqual (panswers3, {"4932 1735937": 5, "11607 1906698": 5, "483 1939265": 1})

main()