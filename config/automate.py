import os
import platform
import subprocess
from typing import Optional, Dict

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


class Browser:
    """
    浏览器
    """

    _loading_data = {
        'Linux': {
            'Chrome': {
                'driver': '/home/python/.wdm/drivers/chromedriver/linux64/chromedriver',
                'version': r'google-chrome --version'
            },
        },
        'Windows': {
            'Chrome': {
                'application': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                'driver': r'C:\Users\{user}\.wdm\drivers\chromedriver\win64\{version}\chromedriver-win32\chromedriver.exe',
                'user_data': r'C:\Users\{user}\AppData\Local\Google\Chrome\User Data',
                'remote_data': r'C:\Users\{user}\AppData\Local\Google\Chrome\RemoteData',
                'version': r'reg query HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon /v version'
            },
        },
    }

    def __init__(
            self,
            loading: bool = False,
            headless: bool = False,
            download: Optional[str] = None,
            driver_path: Optional[str] = None,
    ):
        self.loading = loading
        self.headless = headless
        self.download = download
        self.driver_path = driver_path
        self.system = platform.system()
        self.loading_user = os.getlogin()
        self.loading_data = self._loading_data_config()

    def chrome(self) -> webdriver.Chrome:
        """
        生成chrome
        """
        user_data = self.loading_data['Chrome']['user_data']
        driver_path = self._get_driver_path('Chrome')
        options = ChromeOptions()
        if self.headless:
            options.add_argument('--headless')
        if self.loading:
            if not os.path.exists(user_data):
                raise FileNotFoundError(f'{user_data} not found')
            options.add_argument(f"user-data-dir={user_data}")

        options.add_experimental_option(
            'prefs', {'profile.default_content_settings.popups': 0, 'download.default_directory': self.download})
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--disable-gpu')
        options.add_argument('--hide-scrollbars')
        options.add_argument('blink-setting=imagesEnable=False')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        return webdriver.Chrome(service=ChromeService(driver_path), options=options)

    def remote_chrome(self, host: str = '127.0.0.1', port: int = 1128) -> webdriver.Chrome:
        import socket
        from multiprocessing import Process
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
            if sk.connect_ex((host, port)) != 0:
                Process(target=self._start_remote_chrome, args=(host, port)).start()
        options = ChromeOptions()
        options.add_experimental_option("debuggerAddress", f"{host}:{port}")
        return webdriver.Chrome(options=options)

    def _start_remote_chrome(self, host: str, port: int) -> Optional:
        print(f'启动Chrome远程浏览器: host: {host}, port: {port}')
        loading_data = self.loading_data['Chrome']
        remote_data = loading_data['remote_data']
        os.makedirs(remote_data, exist_ok=True)
        subprocess.Popen(
            [loading_data['application'], f'--remote-debugging-port={port}', f'--user-data-dir={remote_data}'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

    def _get_driver_version(self, browser: str) -> str:
        """
        获取浏览器的版本
        """
        process = subprocess.Popen(
            self._loading_data[self.system][browser]['version'].split(' '),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True
        )
        stdout, stderr = process.communicate()
        if stderr:
            raise SystemError(stderr)
        version = stdout.strip().split()[-1]
        return version

    def _loading_data_config(self) -> Dict:
        configs = self._loading_data[self.system]
        for browser, config in configs.items():
            version = self._get_driver_version(browser)
            for key, value in config.items():
                config[key] = value.format(user=self.loading_user, version=version)
        return configs

    def _get_driver_path(self, browser: str = None) -> str:
        """
        获取驱动路径
        """
        if self.driver_path:
            return self.driver_path

        driver_path = self.loading_data[browser]['driver']
        return driver_path if os.path.exists(driver_path) else ChromeDriverManager().install()


if __name__ == '__main__':
    Browser().remote_chrome()
