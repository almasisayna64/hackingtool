import logging

class HackingTool(object):
    # Остальной код остается без изменений
    
    def __init__(self, options = None, installable: bool = True,
                 runnable: bool = True):
        options = options or []
        if isinstance(options, list):
            self.OPTIONS = []
            if installable:
                self.OPTIONS.append(('Install', self.install))
            if runnable:
                self.OPTIONS.append(('Run', self.run))
            self.OPTIONS.extend(options)
        else:
            raise Exception(
                "options must be a list of (option_name, option_fn) tuples")
        # Добавляем настройку логирования
        logging.basicConfig(filename='hacking_tool.log', level=logging.INFO)

    def install(self):
        self.before_install()
        if isinstance(self.INSTALL_COMMANDS, (list, tuple)):
            for INSTALL_COMMAND in self.INSTALL_COMMANDS:
                os.system(INSTALL_COMMAND)
                logging.info(f"Installed command: {INSTALL_COMMAND}")
            self.after_install()
            logging.info("Installation completed successfully.")

    def uninstall(self):
        if self.before_uninstall():
            if isinstance(self.UNINSTALL_COMMANDS, (list, tuple)):
                for UNINSTALL_COMMAND in self.UNINSTALL_COMMANDS:
                    os.system(UNINSTALL_COMMAND)
                    logging.info(f"Uninstalled command: {UNINSTALL_COMMAND}")
            self.after_uninstall()
            logging.info("Uninstallation completed successfully.")

    def run(self):
        self.before_run()
        if isinstance(self.RUN_COMMANDS, (list, tuple)):
            for RUN_COMMAND in self.RUN_COMMANDS:
                os.system(RUN_COMMAND)
                logging.info(f"Executed command: {RUN_COMMAND}")
            self.after_run()
            logging.info("Execution completed successfully.")
