import sys
from core.wallet_parser import WalletParser
from core.berkeley_inspector import BerkeleyInspector
from crypto.aes_analyzer import AESAnalyzer
from crypto.kdf_analyzer import KDFAnalyzer
from entropy.entropy_profile import EntropyProfiler
from integrity.corruption_detector import CorruptionDetector
from report.json_report import JSONReport


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py wallet.dat")
        sys.exit(1)

    wallet_path = sys.argv[1]

    parser = WalletParser(wallet_path)
    inspector = BerkeleyInspector(wallet_path)
    aes = AESAnalyzer(wallet_path)
    kdf = KDFAnalyzer()
    entropy = EntropyProfiler(wallet_path)
    integrity = CorruptionDetector(wallet_path)

    report = {
        "wallet_info": parser.parse(),
        "berkeley_db": inspector.inspect(),
        "encryption": aes.analyze(),
        "kdf_analysis": kdf.analyze(),
        "entropy": entropy.profile(),
        "integrity": integrity.check(),
    }

    JSONReport(report).save("analysis_report.json")
    print("[+] Analysis completed. Output: analysis_report.json")


if __name__ == "__main__":
    main()

