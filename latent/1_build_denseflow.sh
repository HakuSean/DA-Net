# update the submodules: Caffe and Dense Flow
git submodule update --remote

# build dense_flow
echo "Building Dense Flow"
cd lib/dense_flow
[[ -d build ]] || mkdir build
cd build
OpenCV_DIR=~/Programs/temporal-segment-networks/3rd-party/opencv-2.4.13/build/ cmake .. -DCUDA_USE_STATIC_CUDA_RUNTIME=OFF
if make -j ; then
    echo "Dense Flow built."
else
    echo "Failed to build Dense Flow. Please check the logs above."
    exit 1
fi
