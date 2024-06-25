import pywhatkit as pw
txt = """Writing is a vital skill in university classes, whether you’re majoring in history or business management, economics or engineering. In this course, you’ll learn how to write effectively in different academic formats, especially essays and longer research papers. You’ll learn how to choose a topic for a paper, how to find reliable resources for writing it"""

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])

handwriting_image.save("handwriting.png")
print(" END ")