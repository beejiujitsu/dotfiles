set fish_greeting ""
set -l configdir ~/.config

# because fish complains if a path doesn't exist

for path in /snap/bin $HOME/bin $HOME/.local/bin $HOME/go/bin /opt/local/bin /usr/local/bin $HOME/Library/Python/2.7/bin $HOME/.local/bin /usr/local/opt/coreutils/libexec/gnubin /opt/local/Library/Frameworks/Python.framework/Versions/3.7/bin $HOME/.npm-global/bin $HOME/.krew/bin $HOME/Library/Python/3.8/bin $HOME/Library/Python/3.9/bin $HOME/.gem/ruby/2.6.0/bin
  if test -d $path
    set -x PATH $path $PATH
  end
end


set -x GOPATH $HOME/go

# direnv
#direnv hook fish | source

# Powerline config
if status is-interactive
  for path in $HOME/.local/lib/python3.7/site-packages/powerline/bindings/fish $HOME/Library/Python/3.8/lib/python/site-packages/powerline/bindings/fish
    if test -d $path
      set fish_function_path $fish_function_path $path
      powerline-setup
    end
  end
end

source $configdir/fish/fundle.fish

# Fish config
#
set -g async_prompt_inherit_variables all
#set -g theme_display_git_dirty no
#set -g theme_display_git_untracked no


# Environment variables

#set -x DOCKER_HOST ssh://mark@shannara
#set -x SSH_AUTH_SOCK "$XDG_RUNTIME_DIR/ssh-agent.sock"
set -x EDITOR 'vim'
set -x FIGNORE '*.pyc'
set -x PYTHONDONTWRITEBYTECODE 1
set -x SSL_CERT_FILE '/etc/ssl/cert.pem'
#set -x SSL_CERT_FILE '/opt/local/etc/openssl/cert.pem'

# Aliases
alias ipython "python3 -m IPython"
alias pip "python3 -m pip"
alias f fluxctl
alias k kubectl
alias s ssh
alias m mosh
alias stripcolor "perl -MTerm::ANSIColor=colorstrip -ne 'print colorstrip(\$_)'"
alias pamm $HOME/workspace/source/ammonite/repl
if which ggrep > /dev/null; alias grep ggrep; end
if which gfind > /dev/null; alias find gfind; end
if which gls > /dev/null; alias ls gls; end
alias git-tl "git rev-parse --show-toplevel"
alias pip "python3 -m pip"


#source $configdir/fish/tmux.fish
#source $configdir/fish/flux.fish

function get-shannara
  get-passwd-from-tag-per-session shannara marks | wl-copy
end

function get-ldap
  get-passwd-from-tag-per-session ldap braintree | pbcopy
end

function get-corp
  get-passwd-from-tag-per-session corp braintree | pbcopy
end

function unzip-to --argument-names 'file' 'parentdir'
	set dir (echo $file | awk -F'.zip' '{print $1}')
	unzip $file -d $parentdir/$dir
end

function get-passwd-from-tag-per-session --argument-names 'tags' 'session'
  eval (op signin --session $session); and op list items --tags $tags | op get item --fields password -
end

function cpair-tmux --argument-names 'account'
  set query (tmux list-windows -F '#{window_active} #W' | awk '/^1/{printf $NF}')
  cpair-select $account $query
end

function cpair-select --argument-names 'account' 'query'
  if count $query > /dev/null
    set selected (env CPAIR_ACCOUNT=$account cpair list | fzf --header-lines=1 --query $query)
  else
    set selected (env CPAIR_ACCOUNT=$account cpair list | fzf --header-lines=1)
  end
  echo $selected
  env CPAIR_ACCOUNT=$account cpair ssh -p (echo $selected | awk '{printf $1}')
end

function bt --argument-names 'target_workdir'
  if count $target_workdir > /dev/null
    cd $HOME/bt/$target_workdir
  else
    cd $HOME/bt
  end
end

function work --argument-names 'target_workdir'
  if count $target_workdir > /dev/null
    cd $HOME/workspace/$target_workdir
  else
    cd $HOME/workspace
  end
end

function ipmitool
  /usr/bin/ipmitool -I lanplus -U root -P root -H $argv
end

function vwork --argument-names 'target_workdir'
  if count $target_workdir > /dev/null
    set basedir (string split "/" -- $target_workdir)[1]
    set restofdir (string split --max 1 "/" -- $target_workdir)[2]
    if count $restofdir > /dev/null
      cd /Volumes/Source/$basedir/src/$restofdir
    else
      cd /Volumes/Source/$basedir/src
    end
  else
    cd /Volumes/Source
  end
end


function projdir --argument-names 'name'
  if count $name > /dev/null
    mkdir -pv $name
    touch $name/PROJECT
  end
end

# The next line updates PATH for the Google Cloud SDK.
if test -f '/Users/mshields/Downloads/google-cloud-sdk/path.fish.inc'
  source '/Users/mshields/Downloads/google-cloud-sdk/path.fish.inc'
end

# Extraterm extra integration
if test -f $configdir/fish/extraterm/setup_extraterm_fish.fish
  source $configdir/fish/extraterm/setup_extraterm_fish.fish
end
