#!/bin/bash

set -o pipefail

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
    cd "$1" || return 1
    blue "Judging $1"
    tp_start=$(date +%s)
    if ! judge "$PWD"; then
        return 1
    fi
    tp_end=$(date +%s)

    elapsed_seconds=$(($tp_end - $tp_start))
    elapsed_minutes=$(($elapsed_seconds / 60))
    remaining_seconds=$(($elapsed_seconds % 60))

    if [ $elapsed_minutes -eq 0 ]; then
        yellow "Elapsed time: $remaining_seconds second(s)"
    else
        yellow "Elapsed time: $elapsed_minutes minutes and $remaining_seconds second(s)"
    fi

    cd - || return 1
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
        
        start=$(date +%s)
        python3 main.py < "$file" > "$TMP/$base.$OUTPUT_EXT"
        end=$(date +%s)

        elapsed_seconds=$(($end - $start))
        elapsed_minutes=$(($elapsed_seconds / 60))
        remaining_seconds=$(($elapsed_seconds % 60))

        if diff $TMP/$base.$OUTPUT_EXT "$dir/$TESTS_FOLDER/$base.$ANSWER_EXT" > /dev/null; then
            if [ $elapsed_minutes -eq 0 ]; then
                green "Test $base passed | $remaining_seconds second(s)"
            else
                green "Test $base passed | $elapsed_minutes minute(s) and $remaining_seconds second(s)"
            fi
            passed=$((passed+1))
        else
            if [ $elapsed_minutes -eq 0 ]; then
                red "Test $base failed   | $remaining_seconds second(s)"
            else
                red "Test $base failed   | $elapsed_minutes minute(s) and $remaining_seconds second(s)"
            fi

            failed=$((failed+1))
        fi
    done

    if [ $failed -eq 0 ]; then
        green "All tests passed in $dir"
    else
        red "$failed tests failed in $dir"
    fi 

    rm -rf $TMP

    if [ $failed -eq 0 ]; then
        return 0
    else
        return 1
    fi
}

judge_all() {
    local global_failed=0
    for folder in PL*; do
        if [ -d "$folder" ]; then
            echo
            if ! judge_one "$folder"; then
                global_failed=1
            fi
        fi
    done
    if [ $global_failed -ne 0 ]; then
        return 1
    fi
}

if [ $# -eq 0 ] || [[ "$1" == "all" ]]; then
    judge_all || exit 1
else
    if [ -d "$1" ] || [ -d *-$1 ] || [ -d PL$1* ]; then
        pattern="$1|[A-Za-z0-9]*-$1|PL$1[A-Za-z0-9-]*"
        for file in "$(ls | grep -E ${pattern})"; do
            if ! judge_one $file; then
                exit 1
            fi
        done
    else
        red "$1 is not a directory"
        exit 1
    fi
fi
