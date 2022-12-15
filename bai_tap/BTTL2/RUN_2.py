from doc_ghi_2 import  ghi_sv,doc_sv,in_ra_cac_sv
from bai_tap.sv import SinhVien
def main():
    path = 'F:\\data'
    filename = 'sv4'
    sv1 = [SinhVien('Van Nhi', 2005, 10.0),
           SinhVien('Duy', 2005, 12.0),
           SinhVien('Tri', 2005, 3.0)]
    ghi_sv(path, filename, sv1)
    noidung = doc_sv(path, filename)
    in_ra_cac_sv(noidung)

if __name__ == '__main__':
    main()