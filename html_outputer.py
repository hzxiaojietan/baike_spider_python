class HtmlOutputer(object):
	"""docstring for HtmlOutputer"""
	def __init__(self):
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)


	def output_html(self):
		fout = open('output.html', 'w')
		fout.write('<html>')
		fout.write("<body>")
		fout.write("<table>")

		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>" % data['url'])
			# print("txj==="+data['title'], "txj==="+data['summary'])
			fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
			fout.write("</tr>")

		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")

	def output_txt(self):
		fout = open('output.txt', 'w')
		for data in self.datas:
			fout.write(data['title'].encode('utf-8'))
			fout.write('\n')
			fout.write(data['summary'].encode('utf-8'))

