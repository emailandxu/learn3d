#include "iostream"
#include <Eigen/Dense>

using namespace std;

int main(int argc, char** argv){
    cout << "hello world" << endl;

    Eigen::Matrix<double, 2,3> matrix_23;
    matrix_23 << 1, 2, 3, 4, 5, 6; 
    cout << matrix_23 + Eigen::MatrixXd::Constant(2, 3, 1.2);   
}