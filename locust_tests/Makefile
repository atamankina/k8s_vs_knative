LOCUST = locust -f task_sets.py
#CSV_PREFIX = knative
#CSV_PREFIX = k8s
CSV_PREFIX = hpa
RATE_1 = --clients=1 --hatch-rate=1 --no-web -t 60m
RATE_2 = -c 100 -r 10 --no-web -t 5m
RATE_2A = -c 250 -r 25 --no-web -t 5m
RATE_3 = -c 500 -r 50 --no-web -t 5m
RATE_3A = -c 750 -r 5 --no-web -t 5m
RATE_4 = -c 1000 -r 100 --no-web -t 5m


.DEFAULT_GOAL := help


help:
	@echo "Before running the tests, export the BASE_URL environment variable. \n" \
	"for k8s: http://<IP address>:8080/ \n" \
	"for knative: http://<IP address>/"

test0:
	@echo "Running locust pre-test 1."
	@${LOCUST} ReadSingleObject -c 10 -r 10 --no-web -t 1m --csv=${CSV_PREFIX}_test0

test00:
	@echo "Running locust pre-test 2."
	@${LOCUST} WriteObject -c 10 -r 10 --no-web -t 1m --csv=${CSV_PREFIX}_test00

test000:
	@echo "Running locust pre-test 3."
	@${LOCUST} MultipleReadWrite -c 10 -r 10 --no-web -t 1m --csv=${CSV_PREFIX}_test000

test1:
	@echo "Running locust with parameters: ${RATE_1}"
	@${LOCUST} SingleReadSlow ${RATE_1} --csv=${CSV_PREFIX}_test1

test2:
	@echo "Running locust with parameters: ${RATE_2}"
	@${LOCUST} ReadMultipleEndpoints ${RATE_2} --csv=${CSV_PREFIX}_test2

test3:
	@echo "Running locust with parameters: ${RATE_2}"
	@${LOCUST} MultipleReadWrite ${RATE_2} --csv=${CSV_PREFIX}_test3

test4:
	@echo "Running locust with parameters: ${RATE_3}"
	@${LOCUST} ReadMultipleEndpoints ${RATE_3} --csv=${CSV_PREFIX}_test4

test5:
	@echo "Running locust with parameters: ${RATE_3}"
	@${LOCUST} MultipleReadWrite ${RATE_3} --csv=${CSV_PREFIX}_test5

test6:
	@echo "Running locust with parameters: ${RATE_4}"
	@${LOCUST} ReadMultipleEndpoints ${RATE_4} --csv=${CSV_PREFIX}_test6

test7:
	@echo "Running locust with parameters: ${RATE_4}"
	@${LOCUST} MultipleReadWrite ${RATE_4} --csv=${CSV_PREFIX}_test7

test8:
	@echo "Running locust with parameters: ${RATE_2A}"
	@${LOCUST} ReadMultipleEndpoints ${RATE_2A} --csv=${CSV_PREFIX}_test8

test9:
	@echo "Running locust with parameters: ${RATE_2A}"
	@${LOCUST} MultipleReadWrite ${RATE_2A} --csv=${CSV_PREFIX}_test9

test10:
	@echo "Running locust with parameters: ${RATE_3A}"
	@${LOCUST} ReadMultipleEndpoints ${RATE_3A} --csv=${CSV_PREFIX}_test10

test11:
	@echo "Running locust with parameters: ${RATE_3A}"
	@${LOCUST} MultipleReadWrite ${RATE_3A} --csv=${CSV_PREFIX}_test11