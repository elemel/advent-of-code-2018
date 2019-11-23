for dir in 2018/*
do
	if lua $dir/part_1.lua < ../$dir/input.txt | diff ../$dir/answer_1.txt -
	then
		echo $dir/part_1.lua: PASS
	else
		echo $dir/part_1.lua: FAIL
	fi

	if lua $dir/part_2.lua < ../$dir/input.txt | diff ../$dir/answer_2.txt -
	then
		echo $dir/part_2.lua: PASS
	else
		echo $dir/part_2.lua: FAIL
	fi
done
