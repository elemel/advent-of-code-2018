for day in 2015/* 2016/* 2017/* 2018/*
do
	if [ -f $day/part_1.py ]
	then
		if python3 $day/part_1.py < $day/input.txt | diff $day/answer_1.txt -
		then
			tput setaf 2
			echo $day/part_1.py: PASS
			tput sgr0
		else
			tput setaf 1
			echo $day/part_1.py: FAIL
			tput sgr0
		fi
	fi

	if [ -f $day/part_2.py ]
	then
		if python3 $day/part_2.py < $day/input.txt | diff $day/answer_2.txt -
		then
			tput setaf 2
			echo $day/part_2.py: PASS
			tput sgr0
		else
			tput setaf 1
			echo $day/part_2.py: FAIL
			tput sgr0
		fi
	fi
done
