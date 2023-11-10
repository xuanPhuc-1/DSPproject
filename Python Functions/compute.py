from AudioReader import AudioReader
from SDR import permutation_sdr
from SNR import permute_SI_SNR
import matplotlib.pyplot as plt
import tqdm
import matplotlib.ticker as ticker

# Import thư viện
import os




def main(est_spk1, est_spk2, egs_spk1, egs_spk2):
    est_spk1 = AudioReader(est_spk1)
    est_spk2 = AudioReader(est_spk2)
    egs_spk1 = AudioReader(egs_spk1)
    egs_spk2 = AudioReader(egs_spk2)
    length = len(est_spk1)
    x = [i for i in range(length)]
    sdr = []
    snr = []
    index = 0
    for idx in range(length):
        ests = [est_spk1[idx], est_spk2[idx]]
        egs = [egs_spk1[idx], egs_spk2[idx]]
        mix = egs_spk1[idx]+egs_spk2[idx]

        _snr, per = permute_SI_SNR(ests, egs, mix)
        _sdr = permutation_sdr(ests, egs, mix, per)
    
        index += 1
        if True:
            sdr.append(float(_sdr))
            snr.append(float(_snr))
            print('\r{} : {}, SI-SNRi: {:5f}, SDRi: {:5f}'.format(index, length, _snr, _sdr), end='')

    print('\nAverage SNRi: {:.5f}'.format(float(sum(snr))/len(sdr)))
    print('Average SDRi: {:.5f}'.format(float(sum(sdr)/len(sdr))))


if __name__ == "__main__":
# Đường dẫn đến thư mục chứa các tệp âm thanh WAV
    wav_folder = 'D:/DSPproject/'

    # Tên tệp SCP mà bạn muốn tạo
    scp_file = [
        'test_speech1.scp',
        'test_speech2.scp',
        'test1.scp',
        'test2.scp'
    ]

    # Danh sách các tệp âm thanh WAV
    wav_files = [
        'test_speech1.wav',
        'test_speech2.wav',
        'test1.wav',
        'test2.wav'
    ]

    # Dùng 1 vòng lặp để tạo các tệp SCP
    for i in range(len(scp_file)):
        # Đường dẫn đến tệp SCP
        scp_path = os.path.join(wav_folder, scp_file[i])

        # Đường dẫn đến tệp âm thanh WAV
        wav_path = os.path.join(wav_folder, wav_files[i])

        # Mở tệp SCP để ghi
        with open(scp_path, 'w') as scp:
            # Tạo một khóa (key) từ tên tệp WAV
            key = os.path.splitext(wav_files[i])[0]
            # Viết thông tin vào tệp SCP
            scp.write(f'{key}\t{wav_path}\n')

    est_spk1 = 'test_speech1.scp' #est âm thanh đã được xử lý
    est_spk2 = 'test_speech1.scp' 
    egs_spk1 = 'test1.scp' #âm thanh chưa qua xử lý
    egs_spk2 = 'test1.scp'
    main(est_spk1, est_spk2, egs_spk1, egs_spk2)
