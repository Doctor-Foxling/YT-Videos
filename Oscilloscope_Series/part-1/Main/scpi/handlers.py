from scpi.stateMachine import StateMachine

Sampling = StateMachine()
Chan = StateMachine()
Mode =StateMachine()
Format = StateMachine()

def run_transition(command, protocol):
    if command.upper() == 'RUN':
        if Mode.get_state() == 'RAW':
            newState = Sampling.get_state()
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            print("RAW mode needs to be turned off to start the sampling again")
        newState = 'RUNNING'
    elif command.upper() == 'STOP':
        newState = 'STOPPED'
    else:
        newState = 'errorState'

    return newState

def channel_transition(command, protocol):
    if protocol == 'L':
        if command.upper() == 'CHANNEL1':
            newState = 'CHAN1'
        elif command.upper() == 'CHANNEL2':
            newState = 'CHAN2'
        elif command.upper() == 'CHANNEL3':
            newState = 'CHAN3'
        elif command.upper() == 'CHANNEL4':
            newState = 'CHAN4'
        elif command.upper() == 'MATH':
            if Mode.get_state() == 'RAW' or Mode.get_state() == 'MAX':
                newState = Chan.get_state()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Math channel can't be selected when the RAW or MAX mode is selected")
            newState = 'MATH'
        else:
            newState = 'errorState'
    elif protocol == 'S':
        if command.upper() == 'CHAN1':
            newState = 'CHAN1'
        elif command.upper() == 'CHAN2':
            newState = 'CHAN2'
        elif command.upper() == 'CHAN3':
            newState = 'CHAN3'
        elif command.upper() == 'CHAN4':
            newState = 'CHAN4'
        elif command.upper() == 'MATH':
            if Mode.get_state() == 'RAW' or Mode.get_state() == 'MAX':
                newState = Chan.get_state()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Math channel can't be selected when the RAW or MAX mode is selected")
            newState = 'MATH'
        else:
            newState = 'errorState'
    return newState

def mode_transition(command, protocol):
    if protocol == 'L':
        if command.upper() == 'NORMAL':
            newState = 'NORM'
        elif command.upper() == 'MAXIMUM':
            if Chan.get_state() == 'MATH':
                newState = Mode.get_state()
                print("~~~~~~~~~~~~~")
                print("MAX mode can't be slected when the MATH channel is selected")
            else:
                newState = 'MAX'
        elif command.upper() == 'RAW':
            if Sampling.get_state() == 'RUNNING':
                newState = Mode.get_state()
                print('~~~~~~~~~~~~~~')
                print('-- Sampling needs to be turned off when the RAW mode is to be selected --')
            elif Chan.get_state() == 'MATH':
                newState = Mode.get_state()
                print("~~~~~~~~~~~~~")
                print("RAW mode can't be slected when the MATH channel is selected")
            else:
                newState = 'RAW'
        else:
            newState = "errorState"
        
        return newState
    elif protocol == 'S':
        if command.upper() == 'NORM':
            newState = 'NORM'
        elif command.upper() == 'MAX':
            if Chan.get_state() == 'MATH':
                newState = Mode.get_state()
                print("~~~~~~~~~~~~~")
                print("MAX mode can't be slected when the MATH channel is selected")
            else:
                newState = 'MAX'
        elif command.upper() == 'RAW':
            if Sampling.get_state() == 'RUNNING':
                newState = Mode.get_state()
                print('~~~~~~~~~~~~~~')
                print('-- Sampling needs to be turned off when the RAW mode is to be selected --')
            elif Chan.get_state() == 'MATH':
                newState = Mode.get_state()
                print("~~~~~~~~~~~~~")
                print("RAW mode can't be slected when the MATH channel is selected")
            else:
                newState = 'RAW'
        else:
            newState = "errorState"
        return newState

def format_transition(command, protocol):
    if protocol == 'L':
        if command.upper() == 'WORD':
            newState = 'WORD'
        elif command.upper() == 'BYTE':
            newState = 'BYTE'
        elif command.upper() == 'ASCII':
            newState = 'ASCII'
        else:
            newState = 'errorState'
    elif protocol == 'S':
        if command.upper() == 'WORD':
            newState = 'WORD'
        elif command.upper() == 'BYTE':
            newState = 'BYTE'
        elif command.upper() == 'ASC':
            newState = 'ASCII'
        else:
            newState == 'errorState'
    return newState


