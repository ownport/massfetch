# TODO generate final testing report

test-unittest:
	@ echo '***************************'
	@ echo '*       Unittests         *'
	@ echo '***************************'
	python tests/test_massfetch.py

test-doctest:
	@ echo '***************************'
	@ echo '*       Doctests          *'
	@ echo '***************************'
	python -m doctest tests/test_massfetch.md

test-all:
	make test-unittest
	make test-doctest

todo:
	@ echo 
	@ echo "*** TODOs for massfetch.py ***"
	@ echo 
	@ awk '/# TODO/ { gsub(/^ /, ""); print }' massfetch.py
	@ echo 
	
