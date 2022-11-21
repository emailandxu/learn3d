build:
	mkdir build && cd build && cmake .. && make
run: build
	./build/test_eigen
clean:
	rm -rf build