from doc_ghi_f import  ghi_sv,doc_sv
from bai_tap.sv import SinhVien
def main():
    path = 'F:/data'
    filename = "sv1"
    sv = SinhVien('Van Nhi', 2005, 10.0)
    ghi_sv(path,filename,sv)
    noidung = doc_sv(path,filename)
    if noidung is None:
        print("Xay ra loi")
    else:
        print(noidung)
if __name__ =='__main__':
    main()

