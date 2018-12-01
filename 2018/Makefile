all: build

install:
	/bin/go get -u golang.org/x/lint/golint
	/bin/go get -u honnef.co/go/tools/cmd/megacheck

lint: install
	/bin/go fmt
	/bin/go vet	
	$(GOPATH)/bin/golint -set_exit_status	
	$(GOPATH)/bin/megacheck -unused.exit-non-zero -simple.exit-non-zero -staticcheck.exit-non-zero

build: clean lint
	/bin/go build -o aoc

clean:
	@rm -f aoc

.PHONY: all build install clean
