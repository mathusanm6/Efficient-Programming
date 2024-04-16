#!/bin/bash

#########################################
##  
##  SOURCE: Inspired by Yago Iglesias Vazquez
##  DESCRIPTION: Written with purpose to practice for SWERC.
##
#########################################

TESTS_FOLDER=sample
INPUT_EXT="in"
ANSWER_EXT="out"
OUTPUT_EXT="result"
TMP=./tmp

yellow() {
    printf "\033[33m%s\033[0m\n" "$@"
}

green() {
    printf "\033[32m%s\033[0m\n" "$@"
}

red() {
    printf "\033[31m%s\033[0m\n" "$@"
}

blue() {
    printf "\033[1m\033[34m%s\033[0m\n" "$@"
}

judge_one() {
    cd "$1" || exit
    blue "Judging $1"
    judge "$PWD"
    cd - || exit
}

judge() {
    local dir=$1
    mkdir -p $TMP

    if ! [ -d $dir/$TESTS_FOLDER ]; then
        yellow "No Input Files in $dir"
        return 1
    fi

    if ! [ -f $dir/main.py ]; then
        yellow "main.py file not found in $dir"
        return 1
    fi

    local passed=0
    local failed=0

    for file in $dir/$TESTS_FOLDER/*.$INPUT_EXT; do
        local base=$(basename "$file" .$INPUT_EXT)

        if ! [ -f "$dir/$TESTS_FOLDER/$base.$ANSWER_EXT" ]; then
            red "No answer file for test $base"
            continue
        fi

        python3 main.py < "$file" > "$TMP/$base.$OUTPUT_EXT"
        if diff $TMP/$base.$OUTPUT_EXT "$dir/$TESTS_FOLDER/$base.$ANSWER_EXT" > /dev/null; then
            green "Test $base passed"
            passed=$((passed+1))
        else
            red "Test $base failed"
            failed=$((failed+1))
        fi
    done

    if [ $failed -eq 0 ]; then
        green "All tests passed in $dir"
    else
        red "$failed tests failed in $dir"
    fi 

    rm -rf $TMP
}

judge_all() {
    for folder in PL*; do
        if [ -d "$folder" ]; then
            echo
            judge_one "$folder"
        fi
    done
}

if [ $# -eq 0 ] || [[ "$1" == "all" ]]; then
    judge_all
elif [ -d "$1" ] || [ -d *-$1 ] || [ -d PL$1* ]; then
    pattern="$1|[A-Za-z0-9]*-$1|PL$1[A-Za-z0-9-]*"
    ls | grep -E ${pattern} | while read -r file; do
        judge_one "$file"
    done
else
    red "$1 is not a directory"
fi

