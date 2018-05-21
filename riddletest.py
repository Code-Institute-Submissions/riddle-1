from byotest import *
from riddle import load_data, check_answer, add_user, get_userdb, drop_userdb, get_userdb_p

# load the json data and test it's loaded
data = load_data()
test_are_equal(len(data), 99)
test_are_equal(check_answer(4, "Treat"), True)
test_are_equal(check_answer(4, "TrEaT"), True)
test_are_equal(check_answer(91, "Bubble"), True)

# test the database functions
test_are_equal(get_userdb("mytestuser"), None)
add_user("mytestuser", "password")
test_not_equal(get_userdb("mytestuser"), None)
test_not_equal(get_userdb_p("mytestuser", "password"), None)
drop_userdb("mytestuser")



print("All tests pass")