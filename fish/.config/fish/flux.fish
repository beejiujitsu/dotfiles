# fish completion for completion                           -*- shell-script -*-

function __completion_debug
    set file "$BASH_COMP_DEBUG_FILE"
    if test -n "$file"
        echo "$argv" >> $file
    end
end

function __completion_perform_completion
    __completion_debug "Starting __completion_perform_completion with: $argv"

    set args (string split -- " " "$argv")
    set lastArg "$args[-1]"

    __completion_debug "args: $args"
    __completion_debug "last arg: $lastArg"

    set emptyArg ""
    if test -z "$lastArg"
        __completion_debug "Setting emptyArg"
        set emptyArg \"\"
    end
    __completion_debug "emptyArg: $emptyArg"

    set requestComp "$args[1] __complete $args[2..-1] $emptyArg"
    __completion_debug "Calling $requestComp"

    set results (eval $requestComp 2> /dev/null)
    set comps $results[1..-2]
    set directiveLine $results[-1]

    # For Fish, when completing a flag with an = (e.g., <program> -n=<TAB>)
    # completions must be prefixed with the flag
    set flagPrefix (string match -r -- '-.*=' "$lastArg")

    __completion_debug "Comps: $comps"
    __completion_debug "DirectiveLine: $directiveLine"
    __completion_debug "flagPrefix: $flagPrefix"

    for comp in $comps
        printf "%s%s\n" "$flagPrefix" "$comp"
    end

    printf "%s\n" "$directiveLine"
end

# This function does three things:
# 1- Obtain the completions and store them in the global __completion_comp_results
# 2- Set the __completion_comp_do_file_comp flag if file completion should be performed
#    and unset it otherwise
# 3- Return true if the completion results are not empty
function __completion_prepare_completions
    # Start fresh
    set --erase __completion_comp_do_file_comp
    set --erase __completion_comp_results

    # Check if the command-line is already provided.  This is useful for testing.
    if not set --query __completion_comp_commandLine
        set __completion_comp_commandLine (commandline)
    end
    __completion_debug "commandLine is: $__completion_comp_commandLine"

    set results (__completion_perform_completion "$__completion_comp_commandLine")
    set --erase __completion_comp_commandLine
    __completion_debug "Completion results: $results"

    if test -z "$results"
        __completion_debug "No completion, probably due to a failure"
        # Might as well do file completion, in case it helps
        set --global __completion_comp_do_file_comp 1
        return 0
    end

    set directive (string sub --start 2 $results[-1])
    set --global __completion_comp_results $results[1..-2]

    __completion_debug "Completions are: $__completion_comp_results"
    __completion_debug "Directive is: $directive"

    if test -z "$directive"
        set directive 0
    end

    set compErr (math (math --scale 0 $directive / 1) % 2)
    if test $compErr -eq 1
        __completion_debug "Received error directive: aborting."
        # Might as well do file completion, in case it helps
        set --global __completion_comp_do_file_comp 1
        return 0
    end

    set nospace (math (math --scale 0 $directive / 2) % 2)
    set nofiles (math (math --scale 0 $directive / 4) % 2)

    __completion_debug "nospace: $nospace, nofiles: $nofiles"

    # Important not to quote the variable for count to work
    set numComps (count $__completion_comp_results)
    __completion_debug "numComps: $numComps"

    if test $numComps -eq 1; and test $nospace -ne 0
        # To support the "nospace" directive we trick the shell
        # by outputting an extra, longer completion.
        __completion_debug "Adding second completion to perform nospace directive"
        set --append __completion_comp_results $__completion_comp_results[1].
    end

    if test $numComps -eq 0; and test $nofiles -eq 0
        __completion_debug "Requesting file completion"
        set --global __completion_comp_do_file_comp 1
    end

    # If we don't want file completion, we must return true even if there
    # are no completions found.  This is because fish will perform the last
    # completion command, even if its condition is false, if no other
    # completion command was triggered
    return (not set --query __completion_comp_do_file_comp)
end

# Remove any pre-existing completions for the program since we will be handling all of them
# TODO this cleanup is not sufficient.  Fish completions are only loaded once the user triggers
# them, so the below deletion will not work as it is run too early.  What else can we do?
complete -c completion -e

# The order in which the below two lines are defined is very important so that __completion_prepare_completions
# is called first.  It is __completion_prepare_completions that sets up the __completion_comp_do_file_comp variable.
#
# This completion will be run second as complete commands are added FILO.
# It triggers file completion choices when __completion_comp_do_file_comp is set.
complete -c completion -n 'set --query __completion_comp_do_file_comp'

# This completion will be run first as complete commands are added FILO.
# The call to __completion_prepare_completions will setup both __completion_comp_results abd __completion_comp_do_file_comp.
# It provides the program's completion choices.
complete -c completion -n '__completion_prepare_completions' -f -a '$__completion_comp_results'

