CLUSTER_URL = http://127.0.0.1:5000/
LOCUST = locust -f task_sets.py
CSV_PREFIX = test_run_knative
#CSV_PREFIX = test_run_k8s
RATE_1 = --clients=1 --hatch-rate=0.016 --no-web -t 60m
RATE_2 = -c 100 -r 10 --no-web -t 10m
RATE_3 = -c 500 -r 50 --no-web -t 10m
RATE_4 = -c 1000 -r 100 --no-web -t 10m


test1:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_1}"
	@${LOCUST} SingleReadSlow ${RATE_1} --csv=${CSV_PREFIX}_test1

test2:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_2}"
	@${LOCUST} ReadSingleObject ${RATE_2} --csv=${CSV_PREFIX}_test2

test3:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_2}"
	@${LOCUST} ReadAllObjects ${RATE_2} --csv=${CSV_PREFIX}_test3

test4:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_2}"
	@${LOCUST} ReadMultipleEndpoints ${RATE_2} --csv=${CSV_PREFIX}_test4

test5:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_2}"
	@${LOCUST} WriteObject ${RATE_2} --csv=${CSV_PREFIX}_test5

test6:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_2}"
	@${LOCUST} MultipleReadWrite ${RATE_2} --csv=${CSV_PREFIX}_test6

test7:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_3}"
	@${LOCUST} ReadSingleObject ${RATE_3} --csv=${CSV_PREFIX}_test7

test8:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_3}"
	@${LOCUST} ReadAllObjects ${RATE_3} --csv=${CSV_PREFIX}_test8

test9:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_3}"
	@${LOCUST} ReadMultipleEndpoints ${RATE_3} --csv=${CSV_PREFIX}_test9

test10:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_3}"
	@${LOCUST} WriteObject ${RATE_3} --csv=${CSV_PREFIX}_test10

test11:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_3}"
	@${LOCUST} MultipleReadWrite ${RATE_3} --csv=${CSV_PREFIX}_test11

test12:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_4}"
	@${LOCUST} ReadSingleObject ${RATE_4} --csv=${CSV_PREFIX}_test12

test13:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_4}"
	@${LOCUST} ReadAllObjects ${RATE_4} --csv=${CSV_PREFIX}_test13

test14:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_4}"
	@${LOCUST} ReadMultipleEndpoints ${RATE_4} --csv=${CSV_PREFIX}_test14

test15:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_4}"
	@${LOCUST} WriteObject ${RATE_4} --csv=${CSV_PREFIX}_test15

test16:
	@export BASE_URL=${CLUSTER_URL}
	@echo "Running locust with parameters: ${RATE_4}"
	@${LOCUST} MultipleReadWrite ${RATE_4} --csv=${CSV_PREFIX}_test16