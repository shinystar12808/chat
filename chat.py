# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: #若執行後出現\ufeff，編碼要改成用'utf-8-sig'來去掉
		for line in f:
			lines.append(line.strip()) #去掉換行符號
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines: # 一行一行列印出來
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line =='Tom':
			person = 'Tom'
			continue
		if person: #意即person有值時才運行20-21行
			new.append(person + ': ' + line)	
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main(): #主程式碼
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main() #進入點