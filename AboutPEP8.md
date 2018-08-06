# PEP8 -- Style Guide for Python Code

### What is PEP?
PEP - Python Enhancement Proposal. 

### Why use PEP ?
Khi được phân công vào một nhóm lập trình nào đó, chúng ta cần phối hợp làm việc với các thành viên trong nhóm chứ không làm việc một mình. Vì vậy, code chúng ta viết cần phải theo phong cách, quy định chung để mọi người đều có thể dễ dàng đọc hiểu, kết hợp, kiểm tra, bảo trì và tái sử dụng.<br>
Code được viết theo phong cách chung là thể hiện cách làm việc chuyên nghiệp, cẩn thận, có nguyên tắc
Khi làm việc với ngôn ngữ lập trình nào, nên tuân thủ phong cách lập trình cụ thể của ngôn ngữ đó, tránh việc phối hợp nhiều phong cách trong một ngôn ngữ.<br>
Phong cách lập trình được xem là một “nền văn hóa chung” mà chắc chắn là các lập trình viên cần tìm hiểu “nền văn hóa chung đó”.

## Error codes
This is the current list of error and warning codes:

|code	|sample message|
|----|----|
|E1|	Indentation|
|E101|	indentation contains mixed spaces and tabs|
|E111|	indentation is not a multiple of four|
|E112|	expected an indented block|
|E113	|unexpected indentation|
||| 	 
|E121 (^)	|continuation line indentation is not a multiple of four|
|E122 (^)	|continuation line missing indentation or outdented|
|E123 (*)	|closing bracket does not match indentation of opening bracket’s line|
|E124 (^)|	closing bracket does not match visual indentation|
|E125 (^)|	continuation line does not distinguish itself from next logical line|
|E126 (^)|	continuation line over-indented for hanging indent|
|E127 (^)|	continuation line over-indented for visual indent|
|E128 (^)	|continuation line under-indented for visual indent|
|E133 (*)|	closing bracket is missing indentation|
||| 	 
|E2	Whitespace
|E201|	whitespace after ‘(‘|
|E202|	whitespace before ‘)’|
|E203|	whitespace before ‘:’|
 |||	 
|E211	|whitespace before ‘(‘|
||| 	 
|E221|	multiple spaces before operator|
|E222|	multiple spaces after operator|
|E223	|tab before operator|
|E224	|tab after operator|
|E225	|missing whitespace around operator|
|E226 (*)|	missing whitespace around arithmetic operator|
|E227	|missing whitespace around bitwise or shift operator|
|E228|	missing whitespace around modulo operator|
||| 	 
|E231	|missing whitespace after ‘,’|
||| 	 
|E241 (*)	|multiple spaces after ‘,’|
|E242 (*)	|tab after ‘,’|
||| 	 
|E251	|unexpected spaces around keyword / parameter equals|
|E261	|at least two spaces before inline comment|
|E262	|inline comment should start with ‘# ‘|
||| 	 
|E271|	multiple spaces after keyword|
|E272|	multiple spaces before keyword|
|E273|	tab after keyword|
|E274|	tab before keyword|
|E3	|Blank line|
|E301|	expected 1 blank line, found 0|
|E302	|expected 2 blank lines, found 0|
|E303|	too many blank lines (3)|
|E304|	blank lines found after function decorator|
|||
|E4	|Import|
|E401	|multiple imports on one line|
|E5	Line length
|E501 (^)	|line too long (82 > 79 characters)|
|E502	|the backslash is redundant between brackets|
|E7	|Statement|
|E701	|multiple statements on one line (colon)|
|E702	|multiple statements on one line (semicolon)|
|E703|	statement ends with a semicolon|
|E711 (^)|	comparison to None should be ‘if cond is None:’|
|E712 (^)|	comparison to True should be ‘if cond is True:’ or ‘if cond:’|
|E721	|do not compare types, use ‘isinstance()’|
|E9	|Runtime|
|E901	|SyntaxError or IndentationError|
|E902	|IOError|
 |||	 
|W1	|Indentation warning|
|W191	|indentation contains tabs|
|W2|	Whitespace warning|
|W291|	trailing whitespace|
|W292|	no newline at end of file|
|W293|	blank line contains whitespace|
|W3	|Blank line warning
|W391	|blank line at end of file
|W6	|Deprecation warning|
|W601|	.has_key() is deprecated, use ‘in’|
|W602|	deprecated form of raising exception|
|W603|	‘<>’ is deprecated, use ‘!=’|
|W604	|backticks are deprecated, use ‘repr()’|


__(*)__ In the default configuration, the checks E123, E133, E226, E241 and E242 are ignored because they are not rules unanimously accepted, and PEP 8 does not enforce them. The check E133 is mutually exclusive with check E123. Use switch --hang-closing to report E133 instead of E123.

__(^)__ These checks can be disabled at the line level using the # noqa special comment. This possibility should be reserved for special cases.