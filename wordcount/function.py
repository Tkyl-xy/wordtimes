# from django.http import HttpResponse
#render是传递一个网页给用户
from django.shortcuts import render

def home(request):
	return render(request, "home.html")

def count(request):
	#print()这里是在终端显示的
	# print(len(request.GET['text']))
	user_text = request.GET['text']
	total_count = len(user_text)

	#这里是统计每个字符数出现的次数
	word_dict = {}

	for word in user_text:
		if word not in word_dict:
			word_dict[word] = 1
		else:
			word_dict[word] += 1
	#这里进行字典的排序
	sorte_dict = sorted(word_dict.items(), key=lambda w:w[1], reverse=True)


	#{total_count是总字数}，字典的键count所对应的值都传给count.html文件中
	return render(request, "count.html", \
		{'count':total_count, 'text':user_text, 'times' : sorte_dict})


def about(request):
	return render(request, 'about.html')
	