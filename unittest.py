import unittest
from URLForHost import URLForHost
from xlrd import open_workbook

#--------------------------------------------------------------
# TODO: COMMENTS
#       Write the other tests
#--------------------------------------------------------------

input_0000 = []
expect_0000 = []
input_127 = []
expect_127 = []
input_www = []
expect_www = []
input_side = []
expect_side = []
input_comment = []
expect_comment = []
input_space = []
expect_space = []
input_http = []
expect_http = []


#       getTestData opens an excel file
#       and saves the needed "input" (col 1)
#       and "expect"[ed] output in a list.
#
#       Param:
#      -option: to choose the correct column
#               in the excel file.
#               0000    = col 1
#               127     = col 2
#               www     = col 3
#               side    = col 4
#               comment = col 5
#               space   = col 6
#               http    = col 7
#               all     = for loop (all columns)


def get_test_data(option, input, expect):
    wb = open_workbook(
        "C:\\Users\\Zeus-1\\Desktop\\Stuff"
        "\\Code\\Python\\Projects\\learn\\URLConverter"
        "\\testResources\\input&expected.xlsx")

    activeSheet = wb.sheet_by_index(0)

    col = 0
    if option == "0000":
        col = 1
    elif option == "127":
        col = 2
    elif option == "www":
        col = 3
    elif option == "side":
        col = 4
    elif option == "comment":
        col = 5
    elif option == "space":
        col = 6
    elif option == "http":
        col = 7

    for row in range(activeSheet.nrows):
        if row != 0:
            if option != "all":
                if activeSheet.cell_value(row, col) == "True":
                    input.append(activeSheet.cell_value(row, 0))
                    expect.append(True)
                elif activeSheet.cell_value(row, col) == "False":
                    input.append(activeSheet.cell_value(row, 0))
                    expect.append(False)
                else:
                    input.append(activeSheet.cell_value(row, 0))
                    expect.append(activeSheet.cell_value(row, col))
            else:
                for col in range(activeSheet.nrows):
                    if col < 8:
                        input.append(activeSheet.cell_value(row, 0))
                        expect.append(activeSheet.cell_value(row, col))
                    if col == 8:
                        break


def prepare_data():
    for x in range(8):
        if x == 1:
            input_0000 = []
            expect_0000 = []
            get_test_data("0000", input_0000, expect_0000)
        elif x == 2:
            input_127 = []
            expect_127 = []
            get_test_data("127", input_127, expect_127)
        elif x == 3:
            input_www = []
            expect_www = []
            get_test_data("www", input_www, expect_www)
        elif x == 4:
            input_side = []
            expect_side = []
            get_test_data("side", input_side, expect_side)
        elif x == 5:
            input_comment = []
            expect_comment = []
            get_test_data("comment", input_comment, expect_comment)
        elif x == 6:
            input_space = []
            expect_space = []
            get_test_data("space", input_space, expect_space)
        elif x == 7:
            input_http = []
            expect_http = []
            get_test_data("http", input_http, expect_http)


class TestFunctions(unittest.TestCase):
    prepare_data()

    def test_remove_0000(self):


        i = 0
        for item in input_0000:
            actual = URLForHost.remove_0000(item)
            #print(f"actual: .{actual}.\nexpect: .{TestFunctions.expect[i]}.")
            self.assertEqual(expect_0000[i], actual, "Test failed")
            i += 1

    def test_remove_127(self):
        #get_test_data("127")
        #print("got data from test_remove_127")

        i = 0
        for item in input_127:
            actual = URLForHost.remove_127(item)
            self.assertEqual(expect_127[i], actual, "Test failed")
            i += 1

    def test_remove_www(self):
        #get_test_data("www")
        #print("got data from test_remove_www")

        i = 0
        for item in input_www:
            actual = URLForHost.remove_www(item)
            self.assertEqual(expect_www[i], actual, "Test failed")
            i += 1

    def test_format_for_host(self):
        #self.assertEqual(True, False)
        pass


    def test_zero_or_broadcast(self):
        #self.assertEqual(True, False)
        pass

    def test_open_readfile(self):
        #self.assertEqual(True, False)
        pass

    def test_open_writefile(self):
        #self.assertEqual(True, False)
        pass

    def test_delete_comments(self):
        #get_test_data("side")
        #print("got data from test_delete_comments")

        i = 0
        for item in input_side:
            actual = URLForHost.delete_comments(item)
            self.assertEqual(expect_side[i], actual, "Test failed")
            i += 1

    def test_remove_line_comments(self):
        #get_test_data("comment")
        #print("got data from test_remove_line_comments")

        i = 0
        for item in input_comment:
            actual = URLForHost.remove_line_comments(item)
            self.assertEqual(expect_comment[i], actual, "Test failed")
            i += 1

    def test_remove_space(self):
        #get_test_data("space")
        #print("got data from test_remove_space")

        i = 0
        for item in input_space:
            #print(f"item: '{item}'")
            actual = URLForHost.remove_space(item)
            # print(f"input: {input}\nexpect: {expect}")
            self.assertEqual(expect_space[i], actual, "Test failed")
            i += 1

    def test_remove_http(self):
        i = 0
        for item in input_http:
            # print(f"item: '{item}'")
            actual = URLForHost.remove_http(item)
            # print(f"input: {input}\nexpect: {expect}")
            self.assertEqual(expect_http[i], actual, "Test failed")
            i += 1

    def test_get_uniques(self):
        #self.assertEqual(True, False)
        pass


if __name__ == '__main__':
    unittest.main()
