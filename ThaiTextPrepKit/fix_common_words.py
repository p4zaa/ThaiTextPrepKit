import re
from ThaiTextPrepKit import __version__, vowel_typo

def fix_common_word(x):
    #vowel_typo = '่้๊๋็ีัเ' # ่ ้ ๊ ๋ ็ ี ั เ
    x = re.sub('(ๅ)', 'า', x)
    x = re.sub(f'(แอ[พปฟผ]*[พปฟผ]*ลิเคช[ัี]*[{vowel_typo}]น)|(แอ[{vowel_typo}]*[พปฟผฯ][ฯ]*(?!เปิ[{vowel_typo}]*ล))|(aplication|application|app)', 'แอปพลิเคชัน', x)
    x = re.sub(f'([เแ]อ[{vowel_typo}]*[ปผแบยลำพะฟห][เด้][ปบผ][ิฺอื]*[ลน])', 'แอปเปิ้ล', x)
    x = re.sub('(scan|แสกน)', 'สแกน', x)
    x = re.sub('(time)', 'เวลา', x)
    x = re.sub(f'(ใข้วาน)|([ไใฝำ]*[ชข][{vowel_typo}]*[ง|ว|ฝ][า|ส|่]น)', 'ใช้งาน', x)
    x = re.sub(f'((ใข้ว่าย)|([ไใฝำ]*[ชข][{vowel_typo}]*[งวส][{vowel_typo}]*[่าส]ย))', 'ใช้ง่าย', x)
    x = re.sub(f'(([ไใฝำ]*[ชข][{vowel_typo}]*[นยบ][{vowel_typo}]*[่าส]ก))', 'ใช้ยาก', x)
    x = re.sub('(download|load|ดาว[น]*[์]*[โ]*ห[โ]*ลด|โหลด|หมุน|ดาวโหลด)', 'ดาวน์โหลด', x)
    x = re.sub(f'(net|internet)|([อแิ][อิืฺ์ี]*[รนณฯญย][ดเ้][ทตมคจ][{vowel_typo}]*[แอิ]*[ร]*[ื์]*[รณนฯย]*[ดเ้][รณนฯย][{vowel_typo}]*[คตจทม๖?]*[คตจทม๖?{vowel_typo}]*[คตจทม๖?{vowel_typo}]*)|(เน[{vowel_typo}]*[ตคจทม?๖][ื์]*[ตคจทม?๖]*[ื์]*)', 'อินเทอร์เน็ต', x)
    #x = re.sub('(net|internet|เน็ต|เน๊ต|เนต|เนท|เน็ท|เน๊ท|อินเตอร์เน็ต|อินเตอเนต|อินเตอร์เน็ตต์|อินเทิร์นเน็ต|อินเทิร์เน็ต|อินเทอร์เน็ต์|อินเตอร์เน็ตท์|อินเตอร์เน็ท|อินเตอร์เนท|อินเทอเร็ต|อินเทอร์เนท|อินเทอเน็ต|อินเทอร์เน็ตต์|อินเทอร์เนต|อินเทอร์เน็ท)', 'อินเทอร์เน็ต', x)
    x = re.sub('(account|แอค|แอคฯ|แอคเคาท์|แอ๊ค|แอ๊คฯ|แอกเคาท์|แอ้กเคาท์|แอคเค้า|แอกเค้า|แอกเคา)', 'บัญชี', x)
    x = re.sub('(sms)', 'ข้อความ', x)
    x = re.sub('(atm|adm|ตู้atm|ตู้ atm|เอทีเอ็ม)', 'เครื่องอัตโนมัติ', x)
    x = re.sub('(พ[.]*น[.]*ง[.]*)|(พนง|พนง\.)', 'พนักงาน', x)
    x = re.sub('(system|รบบ)', 'ระบบ', x)
    x = re.sub('(slip|สลิบ)', 'สลิป', x)
    x = re.sub('(error|เออเร่อ)', 'ผิดพลาด', x)
    x = re.sub('(เวิน|ฌงิน|เงิฯ|เงฺน)', 'เงิน', x)
    x = re.sub(f'(ร[ะ]*[ฟหก][ัะีํ๊]ส)', 'รหัส', x)
    x = re.sub(f'(pin|พิ[นณฯ](?!า))|(pwd|pa[s]*sword|pass)|(ร[ะ]*[ฟหกฆ][{vowel_typo}]*[าสว][ฟผป][{vowel_typo}][รนยฯ])|([พภ]า[ร]*[์]*[สดทต][เด้]ว[ิื]*[อ]*[ร]*[์ื]*[กดเตท])', 'รหัสผ่าน', x)
    x = re.sub(f'(อัต[ิ]*โนมัต[ิ]*)', 'อัตโนมัติ', x)
    x = re.sub(f'(เบอ[ร]*[์]*โท[ร]*[สศ]ั[พบ][ท]*[์]*)|(เบอ[ร์]*โท[ร]*)|(เบอ(?!ะ)[ร]*[์]*)', 'หมายเลขโทรศัพท์', x)
    x = re.sub('(ไช้)', 'ใช้', x)
    x = re.sub('(ไช่)', 'ใช่', x)
    x = re.sub('(รุ้)', 'รู้', x)
    x = re.sub('(แล[เ้่]ว)', 'แล้ว', x)
    x = re.sub('([.]*บ[.]*ช[.]*)|(บช\.|บั[น|ร|ณ|ย]ชี)', 'บัญชี', x)
    x = re.sub('(เข้ส)', 'เข้า', x)
    x = re.sub('(ธุระกรมม|ธุระกรม|ธุรกรม|ธุรกรมม|ธุระกรรม|ทุระกรรม|ทุรกรรม|ทุรกรม|ทุรกรมม|ธุกรรม|ทุกรรม)', 'ธุรกรรม', x)
    x = re.sub('(อัพ)', 'อัป', x)
    x = re.sub('(ให่|ไห้|ไห่)', 'ให้', x)
    x = re.sub('(ทันไจ|ทันจัย)', 'ทันใจ', x)
    x = re.sub(f'(ปั[{vowel_typo}]*[ญยนณรสบฯ]หา)', 'ปัญหา', x)
    x = re.sub('(อัพเดท|อัพเดต|อัปเดท|อัปเกรด|update|upgrade)', 'อัปเดต', x)
    x = re.sub('(สะดวด|สดวก|สดวด|สกวก|สะกวก|สพกวก|สพดวก|convenient|convenience)', 'สะดวก', x)
    x = re.sub('(login|log-in|ล็อคอิน|ล็อกอิน|ลอกอิน|ล้อกอิน|ลอคอิน|ล้อคอิน)', 'เข้าใช้งาน', x)
    x = re.sub(f'(ลวดเร็ว|ลวดเล็ว|รวดเล็ว|ดรดเร็ว|รวดเรว|รวดดร็ว|รวดเร้ว|fast|พรวดเร็ว)|เ[ลร][{vowel_typo}]*[กดเ]*[กดเ][ลร][{vowel_typo}]*ว|([พ]*[พรล]ว[เด้]*[แเด้][รล][{vowel_typo}]*ว)', 'รวดเร็ว', x)
    x = re.sub('(เร้ว|ดร็ว|ดรว|เรว)', 'เร็ว', x)
    x = re.sub('(อย่างง(?!ง))', 'อย่าง', x)
    x = re.sub('(อย่างงง+)', 'อย่างงง', x)
    x = re.sub('((อย่าง?!)งง+)', 'งง', x)
    x = re.sub('(บริ[กด][ารส่]*[รนฯยญณ])', 'บริการ', x)
    x = re.sub('(เหตการ|เหตการณ์)', 'เหตุการณ์', x)
    #x = re.sub('(การ|ผม|คับ|ครับ|ค่ะ|ที่|ก็|ก้|ก้อ|โดย|ด้วย|ใน|เป็น|นะ|ฯลฯ)', '', x)
    x = re.sub('(มาก+)', 'มาก', x)
    x = re.sub('()', '', x)
    x = re.sub('(เกณ|เกฑณ์|เกฑ์|เกณ์|เกณณ์|เกนณ[์|ื]*|เกนฑ[์|ื]*)', 'เกณฑ์', x)
    x = re.sub('(call center|callcenter|คอนเซ็นเตอร์|คอลเซนเตอ|คอลเซ็นเตอ|คอลเซลเตอ|คอลเซ็ลเตอ)', 'คอลเซ็นเตอร์', x)
    x = re.sub(f'([ๆไใำ]ม[{vowel_typo}]*[ๆไใำ]ด[{vowel_typo}]*)|(มั[{vowel_typo}]*ย[ๆไใำ]ด[{vowel_typo}]*)|(มั[{vowel_typo}]*ยดั[{vowel_typo}]*ย)|(มั[{vowel_typo}]*ยด[{vowel_typo}]*าย)|(มั[{vowel_typo}]*ยดร[{vowel_typo}]*[า]*ย)|([ๆไใำ]ม[{vowel_typo}]*ด[{vowel_typo}]*าย)|([ๆไใำ]*ม[{vowel_typo}]*[ะ]*(ด[{vowel_typo}]*าย|ดร[{vowel_typo}]*[า]*ย|[ๆไใำ]ด[{vowel_typo}]*))|(บ่(ด[{vowel_typo}]*าย|ดร[{vowel_typo}]*[า]*ย|[ๆไใำ]ด[{vowel_typo}]*))', 'ไม่ได้', x)
    x = re.sub(f'(ล[{vowel_typo}][า]*ช[{vowel_typo}]*[า]*)', 'ล่าช้า', x)
    x = re.sub(f'([โดเก]ค[ห]*[วสงย][ิื]*[{vowel_typo}]*[ดคตท]*[- ]*19)|(covid[ ]*19)', 'covid-19', x)
    x = re.sub(f'([ตคจ][{vowel_typo}]*[อิแ]*[{vowel_typo}]*[วง][กดห][่าส][รนี])', 'ต้องการ', x)
    return x
