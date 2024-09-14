import sys
from matplotlib import pyplot as plt


class Plotter():
    def __init__(self, save_pic_flag):
        self._save_pic_flag = save_pic_flag

    def set_title(self, title, x, y):
        if not self._save_pic_flag:
            return
        plt.cla()
        plt.title(title)
        plt.xlabel(x)
        plt.ylabel(y)

    def plot(self, x, ys, label, scatter=False):
        if not self._save_pic_flag:
            return
        color = ['green', 'blue', 'red', 'black', 'yellow']
        i = 0
        for y in ys:
            if scatter:
                plt.scatter(x, y, s=10.0, color=color[i], label=label[i])
            else:
                plt.plot(x, y, color=color[i], label=label[i])
            plt.legend()
            i = i + 1

    def show(self):
        plt.show()

    def save_pic(self, pic_name):
        if not self._save_pic_flag:
            return
        plt.savefig(pic_name)


class Iperf3LogHandler():
    def __init__(self, file_path_name):
        self._file_path_name = file_path_name
        # unit 1Mbits/sec
        self._bandwidth_data = []

    def _get_bandwidth_data(self):
        return self._bandwidth_data

    def _analysis(self):
        with open(self._file_path_name, 'r') as fd:
            # count = 0
            for strline in fd:
                strdatas = strline.split()
                if 'bits/sec' in strdatas:
                    value = float(strdatas[strdatas.index('bits/sec') - 1]) / 1024 / 1024
                    self._bandwidth_data.append(value)
                elif 'Kbits/sec' in strdatas:
                    value = float(strdatas[strdatas.index('Kbits/sec') - 1]) / 1024
                    self._bandwidth_data.append(value)
                elif 'Mbits/sec' in strdatas:
                    value = float(strdatas[strdatas.index('Mbits/sec') - 1])
                    self._bandwidth_data.append(value)
                # count = count+1
                # if count > 4 :
                #     break


def main(argv):
    handler = Iperf3LogHandler(argv[0])
    handler._analysis()

    bandwidth_data = handler._get_bandwidth_data()
    max_bandwidth_data = max(bandwidth_data)
    min_bandwidth_data = min(bandwidth_data)
    avg_bandwidth_data = sum(bandwidth_data) / len(bandwidth_data)

    print('Max:{}Mbits/sec Min:{}Mbits/sec Average:{}Mbits/sec'.format(max_bandwidth_data, min_bandwidth_data,
                                                                       avg_bandwidth_data))

    plotter = Plotter(True)
    plotter.set_title("The bandwith of XXX", "Time(seconds)", "Bandwith(Mbits/s)")
    plotter.plot(range(len(bandwidth_data)), [bandwidth_data], ['bandwith'], False)
    plotter.save_pic("bandwith.png")
    plotter.show()


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print("usage: data-file")