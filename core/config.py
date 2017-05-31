# Language
lang = "fi"

# Enable log
enable_log = False

# Review mode
review = True

# Don't send changes to wikipedia
test = False

# Don't save if warnings
pass_warnings = True

# Log pages with warnings
log_warnings = False

# Algorithms execute order
algorithms = ["ucc", "brfix",
	"centerfix", "smallfix", "titlechanger",
	"textinen", "seealsotoexl", "twovlines",
	"typofix", "reftosrc", "titlelevel",
	"refstemp", "fix2brackets", "filedelinker",
	"fixpiped", "fixreflist", "replacecomms", "replacesrc", "replaceseealso",
	"replaceli",]

algorithms0 = ["url_fixer"]

# Cat adder
#algorithms = ["catadder"]

# Ignore algorithms
ignore = ["typofix", "ucc", "fixblinks", "fixreflinks", "filedelinker"]

# Warnings
warnings = ["refsec", "secorder", "srcsrefsec", "danreftemp", "titlewithoutcontent", "level3srcs", "catnotbelow", "toomanyrefs", "comments"]

# Ignore warnings
ignore_war = [""]

# Precheck warnings
pre_war = ["notvalidsec"]

# Ignore precheck
pre_ignore = []
