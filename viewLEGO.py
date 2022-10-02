import LEGOStore as lego

def showMainMenu():
    try:
        flag = True
        while flag:
            print("*******************************************************")
            print("**                                                   **")
            print("**                      WELCOME                      **")
            print("**                    LEGO STORE                     **")
            print("**                                                   **")
            print("*************************MENU**************************")
            print("**                                                   **")
            print("**  1. Hiển thị danh sách LEGO có trong Store        **")
            print("**  2. Tìm kiếm bộ Lego theo ID                      **")
            print("**  3. Tìm kiếm bộ Lego theo NAME                    **")
            print("**  4. Thêm mới bộ LEGO                              **")
            print("**  5. Cập nhật bộ LEGO theo ID.                     **")
            print("**  6. Xóa LEGO ra khỏi store                        **")
            print("**  7. Xem tổng giá trị đơn hàng đang có trong store **")
            print("**  8. Sắp xếp LEGO theo thứ tự GIÁ tăng dần         **")
            print("**  9. Sắp xếp LEGO theo thứ tự GIÁ giảm dần         **")
            print("**  0. Thoát                                         **")
            print("**                                                   **")
            print("*******************************************************\n")
            
            key = int(input("Mời bạn nhập: => "))
            
            legoIns = lego.LEGOStore()


            if (key == 1):
                print("\n\n||||====Hiển thị danh sách LEGO====||||")
                legoIns.show()
                
            elif (key == 2):
                print("||||====Tìm kiếm sản phẩm theo ID====||||")
                _id = input("\nNhập ID mà bạn muốn tìm kiếm: => ")
                legoIns.findById(_id)
                print("Successfully Searched!!!\n\n\n\n")
                
            elif (key == 3):
                print("||||====Tìm kiếm sản phẩm theo Tên====||||")   
                name = input("\nNhập tên mà bạn muốn tìm kiếm: => ") 
                legoIns.findByName(name)
                print("Successfully Searched!!!\n\n\n\n")
                
            elif (key == 4):
                print("\n||||====Thêm bộ LEGO mới====||||")
                name_product = input("Nhập tên sp : => ")
                price = int(input("Nhập giá sp : => "))
                brand = input("Nhập nhãn hiệu: => ")
                sku = input("nhập mã sku: => ")
                description = input("Nhập mô tả: => ")
                
                legoIns.insert(name_product, price, brand, sku, description)
                print("")
                
            elif (key == 5):
                print("\n||||====Cập nhật LEGO====||||")
                id = input("Nhập id muốn cập nhật => ")
                
                print("Tiếp theo!!!")
                name_product = input("Nhập tên sp : => ")
                price = int(input("Nhập giá sp : => "))
                brand = input("Nhập nhãn hiệu: => ")
                sku = input("nhập mã sku: => ")
                description = input("Nhập mô tả: => ")
                store_address = input("Nhập địa chỉ: => ")
                
                legoIns.update(id, name_product, price, brand, sku, description, store_address)
                
            elif (key == 6):
                print("\n||||====Xóa sản phẩm LEGO!!!====||||")
                id = input("Nhập id bạn muốn xóa => ")
                
                legoIns.delete(id)
                
            elif (key == 7):
                print("\n||||====Tổng giá trị đơn hàng có trong LEGO Store====||||")
                legoIns.sum()
                
                print("Done Total!")
                
            elif (key == 8):
                print("\n||||====ĐƠN HÀNG SẮP XẾP THEO TĂNG DẦN====||||")
                
                legoIns.orderByPriceASC()
                
            elif (key == 9):
                print("\n||||====ĐƠN HÀNG SẮP XẾP THEO GIẢM DẦN====||||")
                legoIns.orderByPriceDESC()
                
            elif (key == 0):
                print("\nHẸN GẶP LẠI!!!")
                print("THANK YOU!!!")
                break
           
            else:
                flag = True
                print("Mời bạn chọn phím đúng chức năng!!!")
    except:
        print("Đã xảy ra lỗi!!! Bạn hãy kiểm tra lại")
    
showMainMenu()