echo ----------------- input from stdin

echo ----------------- testing illegal parameters
python generate_pursuit.py 0.0 250.0 sides generate_pursuit_err.txt

echo ----------------- generate pursuit triangle
python generate_pursuit.py 0.0 250.0.0 3 > generate_pursuit_triangle.txt
python lines_to_svg.py generate_pursuit_triangle.txt > generate_pursuit_triangle.svg

echo ----------------- generate pursuit square
python generate_pursuit.py 0.0 250.0 4 > generate_pursuit_sqaure.txt
python lines_to_svg.py generate_pursuit_sqaure.txt > generate_pursuit_sqaure.svg

echo ----------------- generate pursuit pentagon
python generate_pursuit.py 0.0 250.0 5 > generate_pursuit_pentagon.txt
python lines_to_svg.py generate_pursuit_pentagon.txt > generate_pursuit_pentagon.svg

echo ----------------- generate pursuit hexagon
python generate_pursuit.py 0.0 250.0 6 > generate_pursuit_hexagon.txt
python lines_to_svg.py generate_pursuit_hexagon.txt > generate_pursuit_hexagon.svg