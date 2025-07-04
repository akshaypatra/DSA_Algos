package Java.Tree.BinaryTree;

import java.util.LinkedList;
import java.util.Queue;

public class BinaryTree {
    TreeNode root;

    public void BuildTree(){
        root= new TreeNode(1);
        root.left=new TreeNode(2);
        root.right=new TreeNode(3);
        root.left.left=new TreeNode(4);
        root.left.right=new TreeNode(5);

    }

    public TreeNode InputTree(Integer[] nodes){


        // Note : if root is (i) then left node is (2i+1) and right node is (2i+2) .

        if (nodes == null || nodes.length == 0 || nodes[0] == null){
            return null;
        };

        root = new TreeNode(nodes[0]);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        int i = 1;
        while (i < nodes.length) {
            TreeNode current = queue.poll();

            if (i < nodes.length && nodes[i] != null) {
                current.left = new TreeNode(nodes[i]);
                queue.offer(current.left);
            }
            i++;

            if (i < nodes.length && nodes[i] != null) {
                current.right = new TreeNode(nodes[i]);
                queue.offer(current.right);
            }
            i++;
        }

        return root;

    }

    public void Inorder(TreeNode node){
        if(node==null){
            return ;
        }
        Inorder(node.left);
        System.out.print(node.val+" ");
        Inorder(node.right);
    }

    public void Preorder(TreeNode node){
        if(node==null){
            return ;
        }
        System.out.print(node.val+" ");
        Preorder(node.left);
        Preorder(node.right);
    }

    public void Postorder(TreeNode node){
        if(node==null){
            return;
        }
        Postorder(node.left);
        Postorder(node.right);
        System.out.print(node.val+" ");
    }


    public static void main(String[] args) {
        BinaryTree tree=new BinaryTree();
        // tree.BuildTree();
        Integer[] input={1, 2, 3, 7, 4, 8, 5};
        tree.InputTree(input);
        

        System.out.println("Inorder Traversal is : ");
        tree.Inorder(tree.root);
        System.out.println("");

        System.out.println("Preorder Traversal is : ");
        tree.Preorder(tree.root);
        System.out.println("");

        System.out.println("Postorder Traversal is : ");
        tree.Postorder(tree.root);
        System.out.println("");

    }


}
