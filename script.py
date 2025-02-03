from pattern_generator import ComplexPatternGenerator

example_patterns = {
    "Solid Rectangle": "[* ,5],3",
    "Hollow Rectangle": "[* ,5],1,[* ,1,  ,3,* ,1],1,[* ,5],1",
    "Half Pyramid": "[* ,!],6",
    "Inverted Half Pyramid": "[* ,!],6..1",
    "Hollow Inverted Half Pyramid": "[* ,6],1,[* ,1,  ,{!-1},* ,1],4..1,[* ,1],1",
    "Full Pyramid": "[  ,{6-!},*   ,!],6",
    "Inverted Full Pyramid": "[  ,!,*   ,{6-!}],0..5",
    "Hollow Full Pyramid": "[  ,5,* ,1],1,[  ,!,* ,1,  ,{9-!*2},* ,1],4..1,[*   ,6],1",
    "Half Pyramid Numeric": "[! ,!],5",
    "Inverted Half Pyramid Numeric": "[! ,!],5..1",
    "Hollow Half Pyramid Numeric": "[! ,1],1,[1 ,1,  ,!,{!!+2},1],0..2,[! ,5],1",
    "Hollow Full Pyramid Numeric": "[  ,4,! ,1],1,[  ,!,! ,1,  ,{7-!*2},{5-!!} ,1],3..1,[!   ,5],1",
    "Hollow Inverted Half Pyramid Numeric": "[! ,5],1,[{5-!!} ,1,  ,{!-1},5 ,1],3..1,[5 ,1],1",
    "Solid Diamond": "[ ,{5-!},* ,!],1..5..1",
    "Hollow Diamond": "[ ,4,* ,1],1,[ ,{3-!},* ,1,  ,!,* ,1],0..3..0,[ ,4,* ,1],1",
}


if __name__ == "__main__":
    generator = ComplexPatternGenerator(justify_size=True, auto_index=True)
    for pattern_name, pattern_code in example_patterns.items():
        generator.generate(pattern_code, pattern_name)

    generator.print_all()
