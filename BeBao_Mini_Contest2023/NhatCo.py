# Hai bạn An và Bình cùng chơi một trò chơi có tên là "nhặt cờ". Trò chơi diễn ra như sau:
# Ban đầu có n lá cờ. An bắt đầu trước, sau đó tới lượt Bình và 2 người chơi luân phiên nhau cho đến khi trò chơi kết thúc.
# Ở mỗi lượt chơi, người chơi sẽ chọn một số nguyên x (1<=x<=m) và loại bỏ chính xác x lá cờ ra khỏi trò chơi. Sau lượt chơi của ai mà tất cả 
# n lá cờ đều bị loại bỏ thì trò chơi kết thúc và người đó sẽ giành chiến thắng.
# Với n, m cho trước, hãy xác định người thắng cuộc của trò chơi nếu cả An và Bình đều chơi tối ưu.
# INPUT: Dòng đầu chứa số nguyên T là số truy vấn cần trả lời (số trò chơi mà An và Bình sẽ chơi)
# T  dòng tiếp theo, mỗi dòng chứa hai số nguyên n, m cách nhau bởi dấu cách, là số lá cờ ban đầu và số lá cờ tối đa mỗi người chơi được bốc
# OUTPUT:Xuất ra T dòng, mỗi dòng chứa một ký tự duy nhất là kết quả của trò chơi thứ i là "A" nếu An thắng hoặc "B" nếu Bình thắng

n = int(input())
while n>0:
    a,b = map(int, input().strip().split(" "))
    if a%(b+1)==0:
        print("B")
    else:
        print("A")
    n-=1
