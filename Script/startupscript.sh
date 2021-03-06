# For installing this script:
# 1. copy this file to home directory
# 2. Enable/Disable the features
# 3. Set the installation directory
# 4. Run following command for Linux:
# echo "source ~/.startupscript" >> ~/.bashrc
# for Mac:
# echo "source ~/.startupscript" >> ~/.profile

######################################
# Enable ("1") or Disable ("0") features #
######################################
# This enables easy fMRI environment variable ($EASYFMRI)
export EN_EZFMRI="1"
# This sets python base direcotry based on $ANACON_PATH
export EN_PYTHON="1"
# This enables iPython by default when you run python in terminal
export EN_PYTHON_ALIAS="1"
# This sets AFNI base directory based on $AFNI_PATH
export EN_AFNI="1"
# This sets FSL base directory based on $FSLDIR and then run fsl.sh script
export EN_FSL="1"
# This enables CUDA environment variables
export EN_CUDA="1"
# This enables bash complete for using TAB in terminal
export EN_BASH="1"
# This sets environment variables for old version of midnight commander
export EN_MC="0"
# This enables colorful command prompt in terminal
export EN_COLOR="1"
# Turn it on for OLED/HiDPI display, default is 200x. It is related to easy fMRI setting.
export EN_SCALE="0"
# Turn it on for OLED/HiDPI display, default is 200x. It is related to FSL setting.
export EN_SCALE_WISH="1" # Run FSL with Scale Factor
# Enabling this item for illustrating GIT current status in terminal
export EN_GIT="1"
# Enabling this item for illustrating current Anaconda env in terminal
# Further you can change the Anaconda environment via aenv/denv commands for switching between different versions of Python
export EN_AENV="1"
export RUN_AENV="0"
######################################
# Proxy for terminal                 #
######################################
# Setup these parameters if you are using VPN to connect internet
alias proxyon='export http_proxy=http://127.0.0.1:3213 && export https_proxy=http://127.0.0.1:3213'
alias proxyoff='export http_proxy= && export https_proxy='
######################################
# Directories & Parameters           #
######################################
# This is base dir for Anaconda, easy fMRI, and AFNI
# For root user, you must set it to the normal user home directory such as export INSTALL_DIR="/home/tony", where
# we have install easy fMRI in the normal user home directory
export INSTALL_DIR="$HOME"
# Base directory of FSL
export FSLDIR="/usr/local/fsl"  # for FSL 5.0.1x
# Base direcory of Anaconda (Python 3.7.x)
export ANACON_PATH="$INSTALL_DIR/anaconda3/bin"
# Base direcory of AFNI
export AFNI_PATH="$INSTALL_DIR/abin"
# Base directory of CUDA
export CUDA_HOME="/usr/local/cuda"
# Scale parameter for OLED/HiDPI display
export SCREEN_SCALE=2     # Set it for OLED display, 2 means 200x
# Uncomment this item if you installed FSL via http://neuro.debian.net/
# export FSLDIR="/usr/share/fsl/5.0" # for FSL 5.0.9
# Uncomment this item if you are using an embedded linux in Windows 10 via WSL
# export DISPLAY=:0.0 # Enable for Windows 10
######################################
# Scripts                            #
######################################

######## Easy fMRI
if (( $EN_EZFMRI != "0" )); then
  export EASYFMRI="$INSTALL_DIR/.easyfmri"
fi

######## Python
if (( $EN_PYTHON != "0" )); then
  export PATH="$ANACON_PATH:$PATH"
fi
if (( $EN_PYTHON_ALIAS != "0" )); then
  alias python="python -m IPython"
  alias python3="python -m IPython"
fi
######## AFNI
if (( $EN_AFNI != "0" )); then
  export DYLD_LIBRARY_PATH=/opt/X11/lib/flat_namespace
  export DYLD_FALLBACK_LIBRARY_PATH="$HOME/abin"
  export PATH="/usr/local/bin:$AFNI_PATH:$PATH"
fi
####### FSL
if (( $EN_FSL != "0" )); then
  . $FSLDIR/etc/fslconf/fsl.sh
  export PATH="$FSLDIR/bin:$PATH"
fi

######## QT Scale Factor
if (( $EN_SCALE != "0" )); then
    export QT_SCALE_FACTOR=1
    export QT_AUTO_SCREEN_SCALE_FACTOR=0
    export QT_SCREEN_SCALE_FACTORS=$SCREEN_SCALE
    # Uncomment these parameters if you are using HiDPI with 100x scale in your Linux (GDK/Gnome) setting
    #export GDK_DPI_SCALE=$SCREEN_SCALE
    #export GDK_SCALE=$SCREEN_SCALE
    if (( $EN_SCALE_WISH != "0" )); then
        export FSLWISH="/usr/bin/wish"
    fi
fi

####### CUDA
if (( $EN_CUDA != "0" )); then
  export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$CUDA_HOME/lib"
  export LD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$CUDA_HOME/lib:/usr/local/cuda/lib64"
  export PATH="$CUDA_HOME/bin:$PATH"
  export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/local/cuda/samples/common/inc
fi

####### BASH
if (( $EN_BASH != "0" )); then
  [ -f /usr/local/etc/bash_completion ] && . /usr/local/etc/bash_completion
fi
####### MC
if (( $EN_MC != "0" )); then
  alias mc=". /usr/local/opt/midnight-commander/libexec/mc/mc-wrapper.sh"
fi
####### Define Colors
  C_DEFAULT="\[\033[m\]"
  C_WHITE="\[\033[1m\]"
  C_BLACK="\[\033[30m\]"
  C_RED="\[\033[31m\]"
  C_GREEN="\[\033[32m\]"
  C_YELLOW="\[\033[33m\]"
  C_BLUE="\[\033[34m\]"
  C_PURPLE="\[\033[35m\]"
  C_CYAN="\[\033[36m\]"
  C_LIGHTGRAY="\[\033[37m\]"
  C_DARKGRAY="\[\033[1;30m\]"
  C_LIGHTRED="\[\033[1;31m\]"
  C_LIGHTGREEN="\[\033[1;32m\]"
  C_LIGHTYELLOW="\[\033[1;33m\]"
  C_LIGHTBLUE="\[\033[1;34m\]"
  C_LIGHTPURPLE="\[\033[1;35m\]"
  C_LIGHTCYAN="\[\033[1;36m\]"
  C_BG_BLACK="\[\033[40m\]"
  C_BG_RED="\[\033[41m\]"
  C_BG_GREEN="\[\033[42m\]"
  C_BG_YELLOW="\[\033[43m\]"
  C_BG_BLUE="\[\033[44m\]"
  C_BG_PURPLE="\[\033[45m\]"
  C_BG_CYAN="\[\033[46m\]"
  C_BG_LIGHTGRAY="\[\033[47m\]"

###### Anaconda envs
if (( $EN_AENV != "0" )); then
env_var=""
## Activate env (default env = base)
aenv() {

    if [ -z $1 ];
    then
        ENV="base"
    else
        ENV="${1}"
    fi

    source activate ${ENV}

    env_var="${ENV}"
}

## Deactivate env
denv() {
    source deactivate
    env_var=""
}

## Information env
ienv() {
    if [[ ${env_var} == "" ]]
    then
        echo ""
    else
        echo "${env_var}"
    fi
}
fi

####### Git Prompt
if (( $EN_GIT != "0" )); then
parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

git_info() {
   echo "$(parse_git_branch)"
}
fi


####### BASH SETUP
if (( $EN_COLOR != "0" )); then
  export PS1=""
# Set Terminal Colors
  export CLICOLOR=1
  alias ls='ls -GFh'
  export LSCOLORS=GxacCxDxBxegedabagaced
# Root User
  if (( $EUID != 0 )); then
    export LSCOLORS=GxacCxDxBxegedabagaced
    export PS1+="$C_LIGHTGREEN\u$C_DEFAULT@$C_LIGHTCYAN\h$C_DEFAULT:$C_LIGHTBLUE\W"
  else
    export PS1+="$C_LIGHTPURPLE\u$C_DEFAULT@$C_LIGHTCYAN\h$C_DEFAULT:$C_LIGHTBLUE\W"
  fi
  if (( $EN_GIT != "0" )); then
# Git Information
    PS1+='\[\033[01;31m\]$(parse_git_branch)'
  fi
# Prompot Symbol
  PS1+="$C_DEFAULT\$$C_LIGHTYELLOW "
fi

####### Run Anaconda env in startup
if (( $RUN_AENV != "0" )); then
  aenv
fi
