from flask import Flask, render_template
app = Flask(__name__)
gl = [
{
'name' : "Out Last",
"desciption" : "Outlast là trò chơi điện tử thuộc thể loại kinh dị sinh tồn được phát triển và phát hành bởi hãng Red Barrels từ Canada dưới dạng góc nhìn người thứ nhất. Outlast kể về cuộc phiêu lưu của nhà báo tự do Miles Upshur nhằm khám phá những bí ẩn bên trong một bệnh viện tâm thần nằm sâu bên trong dãy núi Lake County, Colorado. Bản mở rộng Whistleblower kể về Waylon Park - người đã gửi thư mong Miles đến để điều tra sự thật (về dự án Walrider)",
"image" : "http://tructiepgame.com/wp-content/uploads/2016/08/Whistleblower_promo.png",
},
{
"name" : "NidHogg",
"desciption" : "Nidhogg 2 là hậu bản của game Nidhogg ra mắt vào năm 2014, trò chơi đã nhận được những đánh giá rất tích cực. Lối chơi của Nidhogg 2 vẫn đi theo phong cách đối kháng 1v1 như phiên bản trước, bạn sẽ đấu tay đôi, tận dụng các vũ khí như kiếm, cung... để hạ gục lần lượt các đối thủ và qua màn.",
"image" : "http://i0.wp.com/shoryuken.com/wp-content/uploads/2017/07/nidhogg-2-logo.jpg?fit=750%2C400&resize=750%2C400",
},

{
"name" : "WarFrame",
"desciption" : "Warframe là một game online 3D thuộc thể loại hành động TPS có đề tài khoa học viễn tưởng với chất lượng đồ họa cao. Mục tiêu của người chơi trong game là thu thập được đủ loại chiến giáp  và trải nghiệm các kiểu chiến đấu khác nhau. Hệ thống phụ bản trong game được xây dựng chi tiết, đem lại cảm giác mạo hiểm chân thực cho người chơi.",
"image" : "http://gosu.vn/data/images/GOSU_NEWS/2013-10/07/Lam/0.jpg",
},

{
"name" : "Dying Light",
"desciption" : " Dying Light là một tựa game sinh tồn lấy đề tài zombie cực kỳ ấn tượng của Techland, cha đẻ series game thế giới mở Dead Island được nhiều game thủ Việt yêu mến. Nếu như Dead Island ít nhiều mang tính chất giải trí và không quá nghiêm trọng thì Dying Light lại khắc họa bối cảnh của một thời kì đầy đen tối khi loài người bị đe dọa bởi đại dịch zombie.",
"image" : "https://i.ytimg.com/vi/V3RfeSKSk_g/maxresdefault.jpg",
},
{
"name" : "Assassins Creed Unity 2",
"desciption" : "Assassin’s Creed: Unity là phiên bản tiếp theo trong series sát thủ đã quá nổi tiếng Assassin’s Creed, ngay từ khi chính thức xuất đầu lộ diện với danh nghĩa phiên bản thứ 5 của dòng game, những gì mà người hâm mộ được chứng kiến là sự choáng ngợp của đồ họa, hệ thống gameplay được cải tiến vượt bậc, hứa hẹn một siêu phẩm hay nhất từ trước đến nay.",
"image" : "http://tructiepgame.com/wp-content/uploads/2016/11/Assassins-Creed-Unity-2.jpg",
},
{
"name" : "ShaDow Warrior",
"desciption" : "Shadow Warrior 2 là tựa game hành động kết hợp bắn súng và chặt chém, trò chơi là một sự cân bằng và kết hợp tuyệt vời giữa Path of Exile và Doom, mang đến cho bạn nhiều lối chơi và phong cách giải trí khác nhau, từ chiến đấu cổ điển với cung và kiếm cho đến vũ trang hiện đại với súng ống, lựu đạn.",
"image" : "http://tructiepgame.com/wp-content/uploads/2016/12/Shadow-Warrior-2-2.jpg",
},
{
"name" : "I'm Alive"'',
"desciption" :  "I Am Alive là tựa game sinh tồn đi theo lối hành động giải đố, khá giống với dòng game Uncharted, cũng có nhưng pha lèo trèo và chiến đấu mạo hiểm, chỉ khác là rừng rậm nay đã được thay thế bằng những tòa nhà chọc trời và Adam không có nhiều thời gian cũng như sức lực bởi mỗi phút trôi qua, anh sẽ phải trả giá bằng lượng stamina ít ỏi của mình.",
"image" : "http://tructiepgame.com/wp-content/uploads/2017/03/3-1.jpg",
}
]
@app.route('/')
def index():
    return render_template('index.html', gamelist = gl)


if __name__ == '__main__':
  app.run( debug=True)
