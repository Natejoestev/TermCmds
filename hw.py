#import main as CU
import TermCmds

hw = TermCmds.Command() #CU.Command()

@hw.main_command
def main(args, kwargs, options):
    if len(options)>0:
        if options[0] in ["h", "help"]:
            print("use empty command for Hello, World.")
            print("use \"name\" subcommand then the name as the first argument for \"Hello, (NAME)\".")
            print("use --h or --help option for this message")
            return
    print("Hello, World!")


@hw.command("name")
def name(args, kwars, options):
    if len(args) == 0:
        hw.arg_error(
            TermCmds.errorTypes.little_args
        )
    print("Hello, "+args[0])

if __name__ == "__main__":
    hw.run()