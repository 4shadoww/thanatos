# Language
lang = "fi"

# Enable log
enable_log = False

# Review mode
review = False

# Don't send changes to wikipedia
test = False

# Don't save if warnings
pass_warnings = False

# Log pages with warnings
log_warnings = True

# Algorithms execute order
algorithms = ["ucc", "brfix",
	"centerfix", "smallfix",
	"textinen", "seealsotoexl", "twovlines",
	"typofix", "reftosrc", "titlelevel",
	"refstemp", "fix2brackets", "filedelinker",
	"fixpiped", "replacecomms", "replacesrc", "replaceseealso",
	"replaceli", "fixreflist",]

# Cat adder
#algorithms = ["catadder"]

# Ignore algorithms
ignore = ["typofix", "ucc", "fixblinks", "fixreflinks", "filedelinker"]

# Warnings
warnings = ["refsec", "secorder", "srcsrefsec", "danreftemp", "titlewithoutcontent", "level3srcs", "catnotbelow", "toomanyrefs"]

# Ignore warnings
ignore_war = [""]

# Precheck warnings
pre_war = ["notvalidsec"]

# Ignore precheck
pre_ignore = []
