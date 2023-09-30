'''
Testing: -
-------
	There are two types of testing: -
		(1) UNIT Testing:  The process of testing whether a particular unit is working properly or not
		(2) Integrating Testing: The process of testing total applications.

UNIT Testing: 
------------
	1. We can perform unit testing by using TestCase class within unittest module. We have to inherite unittest.TestCase class and override 3 methods: -
			(i)		setUp(self)		<--- To setup testing environment
			(ii)	test(self)		<--- To test functionality. We can use any name after using 'test' as prefix
			(iii)	tearDown(self)	<--- To destory testing environment
		
		Run unit test using unittest.main()
	2. Class level test cases will execute only once i.e., setUpClass(cls), tearDownClass(cls) will execute only 1 time.
	3. Selenium is use for automating web testing.
	   PyTest is a popular python testing framework.
	4. Limitation: -
		(i)		Test result will be displayed to the console only.
		(ii)	unittest framework always execute test methods in alphabetical order.
		(iii)	It is not possible to set execution order for testing
	5. Naming Convention of PyTest: -
	   ---------------------------
			1. File name should start or end with 'test'
			2. Class name should start with 'Test'
			3. Method name should start with 'test_'
	6. To execute pytest: py.test -s -v testfilename.py
	7. @pytest.fixture() <---- is only for setUp() and we have to use setUp in every test methods
	   @pytest.yield_fixture()	<--- is only for setUptearDown() and we have to use setUptearDown in every test methods
	   @pytest.yield_fixture(scope='module') <--- is only for setUptearDownClass() and we have to use setUptearDownClass in every test methods
'''