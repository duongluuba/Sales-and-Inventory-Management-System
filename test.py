

from prettytable import PrettyTable
myTable = PrettyTable(["STT", "Mã sinh viên", "Họ và tên", "Điểm thi"])
# Hoặc:
# myTable = PrettyTable()
# myTable.field_names = ["STT", "Mã sinh viên", "Họ và tên", "Điểm thi"]

myTable = PrettyTable(["STT", "Mã sinh viên", "Họ và tên", "Điểm thi"])
myTable.add_row(["1", "HS001", "Nguyễn Ngọc Anh", "8.0"])
myTable.add_row(["2", "HS002", "Đặng Bá Nam", "8.5"])
myTable.add_row(["3", "HS003", "Lê Đức Tú", "7.2"])
myTable.add_row(["4", "HS004", "Mạc Văn Viên", "7.3"])
myTable.add_row(["5", "HS005", "Vũ Đình Toàn", "8.0"])
myTable.add_row(["6", "HS006", "Trần Bá Minh", "9.8"])
myTable.add_row(["7", "HS007", "Ngô Đình Tùng", "8.5"])
myTable.add_row(["8", "HS008", "Đỗ Hữu Nam", "7.7"])
print(myTable)
