import re
from scpi.handlers import *

def Initialize_stateM():
    Sampling.add_state("RUNNING", run_transition)
    Sampling.add_state("STOPPED", run_transition)
    Chan.add_state("CHAN1", channel_transition)
    Chan.add_state("CHAN2", channel_transition)
    Chan.add_state("CHAN3", channel_transition)
    Chan.add_state("CHAN4", channel_transition)
    Chan.add_state("MATH", channel_transition)
    Mode.add_state("NORM", mode_transition)
    Mode.add_state("MAX", mode_transition)
    Mode.add_state("RAW", mode_transition)
    Format.add_state("WORD", format_transition)
    Format.add_state("BYTE", format_transition)
    Format.add_state("ASCII", format_transition)
    
    # Setting the start state
    Sampling.set_start("RUNNING")
    Chan.set_start("CHAN1")
    Mode.set_start("NORM")
    Format.set_start("BYTE")


def parse_long(cmd):
    waveform_cmd = re.compile(':WAveForm:\w+ \w+', re.IGNORECASE)
    single_cmd = re.compile(':\w+',re.IGNORECASE)
    waveform_query = re.compile(':Waveform:\w+\?', re.IGNORECASE)
    protocol = 'L'

    if waveform_cmd.match(cmd):
        print(f"{cmd} is the command")

        com, parameter = cmd.split(None, 1)
        type = com.split(':')[2]
        if type.upper() == 'SOURCE':
            error = Chan.run(parameter, protocol)

            if error is not None:
                print(error)
            print(f"{Chan.get_state()} is the current channel selected")
            return "Success"

        elif type.upper() == 'MODE':
            error = Mode.run(parameter, protocol)
            
            if error is not None:
                print(error)
            print(f'{Mode.get_state()} is the Mode selected')
            return "Success"
            
        elif type.upper() == 'FORMAT':
            error = Format.run(parameter, protocol)

            if error is not None:
                print(error)
            print(f'{Format.get_state()} is the Format selected')
            return "Success"
        else:
            return "WAveform command not recognized"

    elif waveform_query.match(cmd):
        query = cmd.split(':')[2]
        Type = query.split('?')[0]
        
        if Type.upper() == 'SOURCE':
            return Chan.get_state()
        elif Type.upper() == 'MODE':
            return Mode.get_state()
        elif Type.upper() == 'FORMAT':
            return Format.get_state()
        else:
            return "Waveform Query not found"

    elif single_cmd.match(cmd):
        parameter = cmd.split(':')[1]
        if cmd.upper() == ':RUN':
            error = Sampling.run(parameter, protocol)

            if error is not None:
                print(error)
            prin(f"{Sampling.get_state()} is the Sampling state")
            return "Success"
        elif cmd.upper() == ':STOP':
            error = Sampling.run(parameter, protocol)

            if error is not None:
                print(error)
            print(f"{Sampling.get_state()} is the Sampling state")
            return "Success"
        else:
            return "Command not recognized"
    else:
        print(f"{cmd} command not found, make sure you're sticking to the protocol")
        return f"{cmd} command not found, make sure you're sticking to the protocol"




def parse_short(cmd):
    waveform_cmd = re.compile(':WAv:\w+ \w+', re.IGNORECASE)
    single_cmd = re.compile(':\w+', re.IGNORECASE)
    waveform_query = re.compile(':Wav:\w+\?', re.IGNORECASE)
    protocol = 'S'

    if (waveform_cmd.match(cmd)):
        print(f"{cmd} is the command")

        com, parameter = cmd.split(None, 1)
        type = com.split[':'][2]
        if type.upper() == 'SOUR':
            error = Chan.run(parameter, protocol)

            if error is not None:
                print(error)
            print(f"{Chan.get_state()} is the current channel selected")
            return "Success"
        elif type.upper() == 'MODE':
            error = Mode.run(parameter, protocol)

            if error is not None:
                print(error)
            print(f'{Mode.get_state()} is the Mode selected')
            return "Success"
        elif type.upper() == 'FORM':
            error = Format.run(parameter, protocol)

            if error is not None:
                print(error)
            print(f'{Format.get_state()} is the Format selected')
            return "Success"

    elif waveform_query.match(cmd):
        query = cmd.split(':')[2]
        Type = query.split('?')[0]

        if Type.upper() == 'SOUR':
            return Chan.get_state()
        elif Type.upper() == 'MODE':
            return Mode.get_state()
        elif Type.upper() == 'FORM':
            return Format.get_state()
        else:
            return "Waveform Query not found"

    elif single_cmd.match(cmd):
        parameter = cmd.split(':')[1]
        if cmd.upper() == ':RUN':
            error = Sampling.run(parameter, protocol)

            if error is not None:
                print(error)
            prin(f"{Sampling.get_state()} is the Sampling state")
            return "Success"
        elif cmd.upper() == ':STOP':
            error = Sampling.run(parameter, protocol)

            if error is not None:
                print(error)
            print(f"{Sampling.get_state()} is the Sampling state")
            return "Success"
        else:
            return "Command not recognized"
    else:
        print(f"{cmd} command not found, make sure you're sticking to the protocol")
        return f"{cmd} command not found, make sure you're sticking to the protocol"